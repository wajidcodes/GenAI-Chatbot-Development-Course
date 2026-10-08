# Lecture 12 — Agentic AI, Tokens, Pinecone & RAG

## Overview

This lecture introduced agentic AI, tokens, model pricing, Pinecone vector search, and a document question-answering automation in n8n. The practical task uses two connected workflows: one ingests emailed documents into Pinecone, and the other answers email questions using only the uploaded document content.

## Topics Covered

- Agentic AI concepts
- Tokens and token-based model pricing
- Pinecone vector databases
- Embeddings and semantic search
- RAG (Retrieval-Augmented Generation)
- Splitting documents into chunks
- Storing document embeddings in Pinecone
- Connecting Gmail, Pinecone, OpenAI embeddings, and Groq in n8n
- Answering relevant questions and rejecting unrelated ones

## Included Materials

| File | Description |
|------|-------------|
| [notes.md](notes.md) | Lecture concepts and detailed explanation of both workflows |
| [task.md](task.md) | Document-ingestion and document-Q&A assignment |
| [workflows/document-ingestion-workflow.json](workflows/document-ingestion-workflow.json) | Workflow 1: email attachments to Pinecone |
| [workflows/document-qa-workflow.json](workflows/document-qa-workflow.json) | Workflow 2: email question to document-based reply |
| [resources/srs-template.pdf](resources/srs-template.pdf) | Supplied sample PDF for testing ingestion |
| [screenshots/document-ingestion-workflow.png](screenshots/document-ingestion-workflow.png) | Screenshot of Workflow 1 |
| [screenshots/document-qa-workflow.png](screenshots/document-qa-workflow.png) | Screenshot of Workflow 2 |

## Learning Outcome

After this lecture, I can explain how token usage affects AI cost, how documents are chunked and indexed in Pinecone, and how RAG can produce document-grounded email answers.
