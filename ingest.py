import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

DATA_PATH = "data/"
DB_PATH = "vectordb/"

documents = []

print("Loading documents...\n")

# Load files
for file in os.listdir(DATA_PATH):

    path = os.path.join(DATA_PATH, file)

    print(f"Found file: {file}")

    try:

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
            print(f"Loaded PDF: {file}")

        elif file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            documents.extend(loader.load())
            print(f"Loaded TXT: {file}")

    except Exception as e:
        print(f"Error loading {file}: {e}")

print(f"\nTotal documents loaded: {len(documents)}")

# Check empty documents
if len(documents) == 0:
    print("\nNo documents found in data folder!")
    exit()

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store vectors
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=DB_PATH
)

vectordb.persist()

print("\nDocuments indexed successfully!")