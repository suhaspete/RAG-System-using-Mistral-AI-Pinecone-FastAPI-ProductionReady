# RAG System using Mistral AI, Pinecone & FastAPI - Production-Ready

## Overview

This project implements a full end-to-end Retrieval-Augmented Generation (RAG) system that enables intelligent question answering over unstructured documents. The application combines semantic search with large language models to produce accurate, context-grounded responses, reducing hallucinations commonly seen in standalone LLM systems.

The project was initially developed as part of a hackathon and subsequently refined to improve modularity, clarity, and production readiness.

---

## Key Features

- Document ingestion and preprocessing from PDF files
- Text chunking with overlap to preserve semantic context
- Dense vector embedding generation for semantic search
- Scalable vector storage and retrieval using Pinecone
- Context-aware answer generation using the Mistral LLM
- RESTful backend API built with FastAPI
- Modular and extensible RAG pipeline using Haystack

---

## System Architecture

PDF Documents
→ Text Extraction and Chunking
→ Embedding Generation
→ Pinecone Vector Database
→ Query Embedding and Similarity Search
→ Context Retrieval
→ Mistral LLM (Answer Generation)
→ FastAPI Response

---

## Technology Stack

- Programming Language: Python
- Backend Framework: FastAPI
- RAG Framework: Haystack
- Large Language Model: Mistral-7B
- Vector Database: Pinecone
- Embedding Models: Sentence Transformers
- Document Loader: PDF Loader
- Deployment: Local or Cloud-based

---

## Workflow Explanation

### Document Ingestion

PDF documents are loaded and parsed into raw text. The text is split into overlapping chunks to ensure contextual continuity across segments.

### Embedding and Indexing

Each text chunk is converted into a dense vector embedding. These embeddings, along with relevant metadata, are stored in Pinecone to enable fast and scalable similarity search.

### Query Processing

When a user submits a query, the query is embedded using the same embedding model. Pinecone retrieves the most semantically relevant document chunks based on vector similarity.

### Answer Generation

The retrieved document chunks are injected into a structured prompt. The Mistral language model uses this grounded context to generate a concise and accurate response.

---

## How to Run the Project

1. Create and activate a Python environment:

   conda create -n rag-env python=3.9 -y
   conda activate rag-env

2. Install dependencies:

   pip install -r requirements.txt

3. Run the document ingestion pipeline:

   python ingestion.py

4. Start the FastAPI server:

   uvicorn app:app --reload

5. Access the API documentation at:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Improvements Over Basic RAG Implementations

- Clear separation of ingestion, retrieval, and generation layers
- Scalable vector search using a managed vector database
- Clean API design suitable for production environments
- Easy extensibility for model or vector store replacement

---

## Future Enhancements

- Support for multiple document formats
- Source attribution and citation in responses
- Streaming responses for improved user experience
- Evaluation metrics for retrieval and generation quality
- Authentication and role-based access control

---

## Individual Contribution

- Designed the overall RAG system architecture
- Implemented document ingestion and chunking pipeline
- Integrated Pinecone vector database with Haystack
- Built FastAPI endpoints for query handling
- Optimized prompts to improve answer grounding and relevance

---

## Project Context

This project was developed as part of a team during a hackathon. The repository reflects individual contributions and enhancements made post-event to improve clarity, robustness, and readiness for professional use.
