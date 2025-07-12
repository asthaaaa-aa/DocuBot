import argparse
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os


os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"]

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""



llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7
)

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  
) 

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB.
    embedding_function = embedding
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.4:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n-----\n\n".join([doc.page_content for doc, _score in results])

    print("\n📚 Context retrieved:")
    print("════════════════════════════════════════════")
    print(context_text)
    print("════════════════════════════════════════════")
    # print(context_text)
    
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    print("\n📝 Final prompt sent to the model:")
    print("────────────────────────────────────────────")
    print(prompt)
    print("────────────────────────────────────────────")
    # print("🏍🏍🏍🏍 PROMPT ---- \n", prompt)


    print("\n💬 Generating answer from LLM...")

    response = llm.invoke(prompt)


    print("\n✅ Final Answer:")
    print("🌟" * 40)
    print(response.content)
    print("🌟" * 40)
    # print("\n⚡⚡⚡", response.content)

if __name__ == "__main__":
    main()