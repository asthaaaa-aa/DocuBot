DocuBot is a lightweight RAG (Retrieval-Augmented Generation) system that allows you to ask questions from your own `.md` (Markdown) documents using local embeddings and powerful open-source LLMs via OpenRouter.

Built with:
- 🧠 LangChain for orchestration
- 📦 ChromaDB for vector storage
- 🤗 HuggingFace Embeddings
- 💬 Mistral-7B via OpenRouter (free-tier API)
- 🌐 Streamlit frontend for instant interaction

---

Features:

- 🔍 Search `.md` files for relevant context
- 💡 Ask questions in plain English
- 🧠 Get context-aware answers from an LLM
- 🖼️ Simple, elegant frontend with Streamlit
- 🔐 API keys managed via `.env`



# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
