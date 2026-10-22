"""
JobPilot AI - an AI agent that tailors your resume to each job and sends the application
-----------------------------------------------------------------------------------------
The agent follows 4 steps:
  1. COLLECT  - load your master profile (all your skills/projects) and the jobs you picked
  2. ANALYZE  - read each job description, match it with your profile, give a score
  3. ACT      - for good matches: build a tailored resume + application email, then
                (only if you approve) send it to the recruiter
  4. REPORT   - save an application tracker (applications_log.csv) and a summary

Run:  python agent.py
- Uses only Python's standard library (nothing to install).
- Default mode is a SAFE DRY RUN: it writes the files but sends NO emails.
- If ANTHROPIC_API_KEY is set, Claude writes the email text (using only your real facts).
- If EMAIL_USER and EMAIL_APP_PASSWORD are set, it asks "send? (y/n)" before each email.
"""

import csv
import json
import os
import re
import smtplib
import ssl
from datetime import date
from email.message import EmailMessage

PROFILE_FILE = "master_profile.json"
JOBS_FILE = "jobs.json"
OUT_DIR = "applications"
LOG_FILE = "applications_log.csv"
MIN_SCORE = 0.6  # only apply when at least 60% of the job's skills match yours

SKILL_VOCAB = [
    "python", "sql", "machine learning", "deep learning", "nlp", "llm", "langchain", "n8n",
    "rag", "chatbot", "prompt engineering", "fastapi", "docker", "aws", "git", "rest api",
    "pandas", "pytorch", "tensorflow", "javascript", "react", "java", "power bi", "excel",
]


# ---------------------------------------------------------------
# STEP 1: COLLECT DATA
# ---------------------------------------------------------------
def create_sample_data():
    """Practice data. Replace these two files with your real profile and real jobs."""
    profile = {
        "name": "Sample Candidate",
        "email": "you@example.com",
        "linkedin": "linkedin.com/in/your-profile",
        "headline": "Gen AI and chatbot developer",
        "education": "BS Computer Science",
        "skills": ["python", "sql", "nlp", "llm", "langchain", "n8n", "rag", "chatbot",
                   "prompt engineering", "fastapi", "docker", "git", "rest api", "pandas"],
        "highlights": [
            {"title": "Support Chatbot", "skills": ["chatbot", "langchain", "rag", "llm"],
             "text": "Built a customer-support chatbot with LangChain and RAG that answers FAQs from company documents"},
            {"title": "n8n Automations", "skills": ["n8n", "rest api"],
             "text": "Created n8n workflows connecting Gmail, Google Sheets and OpenAI to remove manual work"},
            {"title": "FastAPI Services", "skills": ["fastapi", "docker", "rest api", "python"],
             "text": "Built REST APIs with FastAPI and deployed them using Docker"},
            {"title": "Resume Matcher", "skills": ["python", "nlp"],
             "text": "Wrote a Python NLP tool that compares resumes with job descriptions"},
            {"title": "Sales Dashboard", "skills": ["sql", "pandas", "python"],
             "text": "Analysed sales data with SQL and Pandas and presented insights to managers"},
        ],
    }
    jobs = [
        {"title": "Generative AI Chatbot Developer", "company": "NovaSoft", "url": "https://linkedin.com/jobs/view/111",
         "recruiter_email": "hr@novasoft.example",
         "description": "We need a developer with Python, LangChain, RAG and LLM experience to build chatbots. "
                        "Knowledge of FastAPI and Docker is a plus."},
        {"title": "AI Automation Engineer", "company": "FlowWorks", "url": "https://linkedin.com/jobs/view/222",
         "recruiter_email": "jobs@flowworks.example",
         "description": "Build automations using n8n, REST API integrations and prompt engineering. Python and Git required."},
        {"title": "Machine Learning Engineer", "company": "DeepVision", "url": "https://linkedin.com/jobs/view/333",
         "recruiter_email": "talent@deepvision.example",
         "description": "Looking for strong deep learning skills with PyTorch or TensorFlow, plus Python and AWS."},
        {"title": "Frontend Developer", "company": "PixelHub", "url": "https://linkedin.com/jobs/view/444",
         "recruiter_email": "careers@pixelhub.example",
         "description": "React and JavaScript developer needed. Git and REST API experience welcome."},
    ]
    json.dump(profile, open(PROFILE_FILE, "w"), indent=2)
    json.dump(jobs, open(JOBS_FILE, "w"), indent=2)


def collect():
    if not (os.path.exists(PROFILE_FILE) and os.path.exists(JOBS_FILE)):
        create_sample_data()
        print("[Collect] No data found - created sample profile and jobs")
    profile = json.load(open(PROFILE_FILE))
    jobs = json.load(open(JOBS_FILE))
    print(f"[Collect] Profile for '{profile['name']}' loaded with {len(profile['skills'])} skills")
    print(f"[Collect] {len(jobs)} jobs loaded")
    return profile, jobs


# ---------------------------------------------------------------
# STEP 2: ANALYZE (match every job with the profile)
# ---------------------------------------------------------------
def skills_in_text(text):
    text = text.lower()
    return [s for s in SKILL_VOCAB if re.search(r"\b" + re.escape(s) + r"s?\b", text)]


def analyze(profile, jobs):
    mine = set(profile["skills"])
    for job in jobs:
        required = skills_in_text(job["title"] + " " + job["description"])
        job["required"] = required
        job["matched"] = [s for s in required if s in mine]
        job["missing"] = [s for s in required if s not in mine]
        job["score"] = len(job["matched"]) / len(required) if required else 0
    jobs.sort(key=lambda j: j["score"], reverse=True)
    print("[Analyze] Match scores:")
    for j in jobs:
        decision = "APPLY" if j["score"] >= MIN_SCORE else "SKIP "
        print(f"          {decision} {j['score']:.0%}  {j['title']} @ {j['company']}")
    return jobs


# ---------------------------------------------------------------
# STEP 3: ACT (tailor resume, write email, optionally send)
# ---------------------------------------------------------------
def build_resume(profile, job):
    matched = set(job["matched"])
    skills = sorted(profile["skills"], key=lambda s: (s not in matched, s))  # matched skills first
    best = sorted(profile["highlights"], key=lambda h: -len(set(h["skills"]) & matched))[:4]
    top = ", ".join(job["matched"][:3])
    lines = [
        profile["name"].upper(),
        f"{profile['email']} | {profile['linkedin']}", "",
        "SUMMARY",
        f"{profile['headline']} with hands-on experience in {top}. "
        f"Applying for the {job['title']} role at {job['company']}.", "",
        "KEY SKILLS (most relevant first)", ", ".join(skills), "",
        "RELEVANT EXPERIENCE AND PROJECTS",
    ]
    lines += [f"- {h['title']}: {h['text']}" for h in best]
    lines += ["", "EDUCATION", profile["education"]]
    return "\n".join(lines), best


def write_email(profile, job, best):
    subject = f"Application for {job['title']} - {profile['name']}"
    key = os.getenv("ANTHROPIC_API_KEY")
    if key:
        try:
            import anthropic  # pip install anthropic
            client = anthropic.Anthropic(api_key=key)
            facts = "; ".join(h["text"] for h in best)
            reply = client.messages.create(
                model="claude-sonnet-5-5",
                max_tokens=300,
                messages=[{"role": "user", "content":
                           f"Write a short, polite job application email (max 90 words) from "
                           f"{profile['name']} for the role '{job['title']}' at {job['company']}. "
                           f"Matching skills: {', '.join(job['matched'])}. "
                           f"Use ONLY these true facts, do not invent anything: {facts}. "
                           f"Mention the resume is attached. Sign with the name and email "
                           f"{profile['email']}. Return only the email body."}],
            )
            return subject, reply.content[0].text.strip()
        except Exception as e:
            print(f"[Act] AI call failed ({e}), using template instead")
    body = (
        f"Dear Hiring Team at {job['company']},\n\n"
        f"I am applying for the {job['title']} position. My background matches your needs in "
        f"{', '.join(job['matched'][:4])}. For example: {best[0]['text'][0].lower() + best[0]['text'][1:]}.\n\n"
        f"My resume, tailored for this role, is attached. Thank you for your time.\n\n"
        f"Kind regards,\n{profile['name']}\n{profile['email']}\n{profile['linkedin']}"
    )
    return subject, body


def send_email(to, subject, body, attachment):
    user, password = os.getenv("EMAIL_USER"), os.getenv("EMAIL_APP_PASSWORD")
    if not (user and password):
        return "DRAFTED (dry run)"
    answer = input(f"          Send this application to {to}? (y/n): ").strip().lower()
    if answer != "y":
        return "DRAFTED (not sent)"
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = user, to, subject
    msg.set_content(body)
    with open(attachment, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="plain",
                           filename=os.path.basename(attachment))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(user, password)
        server.send_message(msg)
    return "SENT"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def act(profile, jobs):
    os.makedirs(OUT_DIR, exist_ok=True)
    for job in jobs:
        if job["score"] < MIN_SCORE:
            job["status"] = "SKIPPED (low match)"
            continue
        resume, best = build_resume(profile, job)
        subject, body = write_email(profile, job, best)
        base = os.path.join(OUT_DIR, slug(job["company"]))
        resume_path = base + "_resume.txt"
        open(resume_path, "w").write(resume)
        open(base + "_email.txt", "w").write(
            f"To: {job['recruiter_email']}\nSubject: {subject}\nAttachment: {resume_path}\n\n{body}")
        print(f"[Act] Tailored resume + email created for {job['company']}")
        job["status"] = send_email(job["recruiter_email"], subject, body, resume_path)


# ---------------------------------------------------------------
# STEP 4: REPORT (application tracker)
# ---------------------------------------------------------------
def report(jobs):
    new_file = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["date", "company", "job_title", "match_score", "skills_to_learn", "status", "url"])
        for j in jobs:
            w.writerow([date.today(), j["company"], j["title"], f"{j['score']:.0%}",
                        "; ".join(j["missing"]), j["status"], j["url"]])
    applied = sum(1 for j in jobs if not j["status"].startswith("SKIPPED"))
    gaps = sorted({s for j in jobs for s in j["missing"]})
    print(f"[Report] {applied} applications prepared, {len(jobs) - applied} skipped")
    print(f"[Report] Skills that would unlock more jobs: {', '.join(gaps) if gaps else 'none'}")
    print(f"[Report] Tracker saved to {LOG_FILE}, files saved in the '{OUT_DIR}' folder")


# ---------------------------------------------------------------
# RUN THE AGENT
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== JobPilot AI Agent started ===\n")
    profile, jobs = collect()
    jobs = analyze(profile, jobs)
    act(profile, jobs)
    report(jobs)
    print("\n=== Done! Open the 'applications' folder to see your tailored resumes and emails ===")
