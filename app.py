import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# Config
CHROMA_PATH = "chroma"
DOCS_DIR = "data/books"  # folder for preloaded markdowns
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7
)

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# Streamlit UI
st.title("📘 DocuBot - Chatbot for your Documents!")

# --- File source selection ---
st.subheader("Choose a Markdown File")
available_files = [f for f in os.listdir(DOCS_DIR) if f.endswith(".md")]
selected_file = st.selectbox("📁 Select a sample .md file", available_files)

st.markdown("**OR**")

uploaded_file = st.file_uploader("📤 Upload your own Markdown file", type=["md"])

# Determine file source
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    source_name = uploaded_file.name
    st.success(f"✅ Uploaded file: {source_name}")
elif selected_file:
    file_path = os.path.join(DOCS_DIR, selected_file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    source_name = selected_file
    st.success(f"📄 Selected file: {source_name}")
else:
    st.warning("Please upload or select a markdown file.")
    st.stop()

# Create Document
doc = Document(page_content=content, metadata={"source": source_name})

# Chunk it
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
chunks = splitter.split_documents([doc])

# Temporary Chroma DB for session
with tempfile.TemporaryDirectory() as tmp_chroma_path:
    db = Chroma.from_documents(chunks, embedding)

    query = st.text_input("🔎 Ask something about the document:")

    if query:
        results = db.similarity_search_with_relevance_scores(query, k=3)
        if len(results) == 0 or results[0][1] < 0.4:
            st.warning("⚠️ No relevant results found.")
        else:
            context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
            prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
            prompt = prompt_template.format(context=context_text, question=query)
            response = llm.invoke(prompt)

            st.markdown("### 🤖 Answer")
            st.success(response.content)
