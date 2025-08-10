
# 🤖 DocuBot – AI Chatbot for Documents

An AI-powered **Retrieval-Augmented Generation (RAG)** application that lets you query your Markdown files with natural language. DocuBot uses local embeddings and free-tier LLMs via OpenRouter for fast, context-aware answers—right from your documents.

---

## 🔗 Project Description

This project lets users:

* 📂 Ingest `.md` files as a knowledge base
* 💬 Ask natural-language questions to get context-aware answers
* 🎨 Interact through a clean, responsive Streamlit interface

Built using:

* ⚙️ **LangChain** for orchestration
* 🗄️ **ChromaDB** for vector storage
* 🧠 **HuggingFace** embeddings
* 🤯 **Mistral-7B** via OpenRouter API (free tier)
* 🖥️ **Streamlit** for frontend UI

---

## 🌐 Demo
[https://docu-bot-chat-with-your-docs.streamlit.app/](https://docu-bot-chat-with-your-docs.streamlit.app/)
<img width="960" height="479" alt="home" src="https://github.com/user-attachments/assets/437e54ec-0f2b-4a9c-937c-17b63471b8f5" />
---

## 🚀 Getting Started

### 📥 Clone the Repository

```bash
git clone https://github.com/asthaaaa-aa/DocuBot.git
cd DocuBot
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Environment Variables

Create a `.env` file in the root directory with:

* `OPENROUTER_API_KEY` – OpenRouter API key
* Any other LLM/embedding service keys if needed

### ▶️ Run the App Locally

```bash
streamlit run app.py
```

---

## 🧩 Features

* 📄 Query Markdown documents with plain English
* ⚡ Context-aware responses powered by RAG
* 🎯 Lightweight, self-hosted, and open-source
* 🖌️ Minimal and responsive frontend with Streamlit
* 🔐 Secure API key management via `.env`

---

## 💡 Inspiration

DocuBot was built to **simplify document querying** while exploring **RAG pipelines** using open-source tools. It demonstrates the integration of LangChain, vector databases, and modern LLM APIs to make knowledge retrieval intuitive.

---

## 🛠 Tech Stack

* 🐍 Python
* ⚙️ LangChain
* 🗄️ ChromaDB
* 🧠 HuggingFace embeddings
* 🤯 Mistral-7B via OpenRouter
* 🖥️ Streamlit

---

## 🧪 Potential Improvements

* 📑 Support for `.pdf`, `.docx`, `.txt` files
* 🗂️ Session-based chat history
* 📚 Citation support (document + location)
* 🔍 Search filters by filename or keyword
* 👥 Multi-user authentication
* 📦 Dockerized deployment with CI/CD
