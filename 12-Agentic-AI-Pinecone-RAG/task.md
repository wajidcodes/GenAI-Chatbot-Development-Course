# Assigned Task: Email-Based Document Q&A with Pinecone

Build two connected n8n automations that let a user email a document for indexing, then email questions about that document and receive a relevant answer as an email reply.

## Objective

The system should help handle different ways of expressing the same answer in online assessments or forms. For example, a direct answer such as `I am 21 years old` and an indirect answer such as `I was born in 2005` may need semantic understanding rather than exact keyword matching.

The automation uses embeddings, Pinecone retrieval, and an LLM to interpret the meaning of document-based content. It must not answer questions that are unrelated to the uploaded documents.

## Workflow 1: Ingest Documents into Pinecone

```text
Gmail attachment
  ↓
Extract document text
  ↓
Split into chunks
  ↓
Create embeddings
  ↓
Store vectors in Pinecone
  ↓
Send ingestion confirmation email
```

Use the supplied [document-ingestion workflow](workflows/document-ingestion-workflow.json) as the starting point. It supports PDF, TXT, and DOCX attachments and stores data in the `n8n-document-rag` Pinecone index under the `documents` namespace.

Use the supplied [sample PDF](resources/srs-template.pdf) to test the workflow.

## Workflow 2: Answer Questions by Email

```text
Gmail question email
  ↓
Extract the question
  ↓
Search relevant Pinecone chunks
  ↓
Give chunks to the LLM as context
  ↓
Create document-grounded answer
  ↓
Reply by email
```

Use the supplied [document-Q&A workflow](workflows/document-qa-workflow.json) as the starting point. It retrieves the top five matching chunks and uses Groq to generate an answer.

## Required Behaviour

- If the question is relevant and the answer is supported by the document, reply clearly using the document information.
- If the question is unrelated to the documents, explain that only document-based questions can be answered.
- If relevant information is not found in the retrieved content, say that the documents do not contain enough information.
- Do not allow the model to use unrelated general knowledge as the answer.

## Setup Checklist

- [ ] Pinecone index `n8n-document-rag` created with dimension `3072` and cosine similarity
- [ ] Pinecone namespace set to `documents`
- [ ] Gmail OAuth2 credential configured
- [ ] OpenAI embedding credential configured
- [ ] Groq credential configured
- [ ] Ingestion workflow tested with the sample PDF
- [ ] Confirmation email received after ingestion
- [ ] Relevant question tested
- [ ] Unrelated question tested
- [ ] No API keys or credentials added to GitHub
