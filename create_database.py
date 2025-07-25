from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import openai 
import os
import shutil


DATA_PATH = "data/books"
CHROMA_PATH = "chroma"

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  
) 

def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"\n\nSplit {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[6]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    db = Chroma.from_documents(
        chunks, embedding, persist_directory=CHROMA_PATH
    )
    
    db.persist() #force save
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}." )


if __name__ == "__main__":
    main()