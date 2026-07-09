from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Loading vector database...")

vectorstore = Chroma(
    persist_directory="vectordb",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

print("Loading Llama 3...")

llm = ChatOllama(
    model="llama3",
    temperature=0
)

print("Ready!")

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer the user's question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print("-" * 50)
    print(response.content)