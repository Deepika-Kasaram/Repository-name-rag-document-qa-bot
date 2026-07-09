# 🤖 RAG Document QA Bot using LangChain, ChromaDB & Ollama

An **Offline Retrieval-Augmented Generation (RAG)** chatbot that answers questions from your documents using **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **Ollama (Llama 3)**.

Unlike cloud-based solutions, this project runs **completely offline**, ensuring privacy, zero API costs, and fast document retrieval.

---

## 🚀 Features

- 📄 Supports PDF and TXT documents
- 🔍 Semantic document search using ChromaDB
- 🧠 HuggingFace sentence-transformer embeddings
- 🤖 Local LLM with Ollama (Llama 3)
- 🔒 100% Offline (No OpenAI/Gemini API required)
- ⚡ Fast document retrieval
- 📚 Retrieval-Augmented Generation (RAG)
- 💻 Command Line Interface (CLI)

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangChain | RAG Framework |
| ChromaDB | Vector Database |
| HuggingFace | Text Embeddings |
| Sentence Transformers | Semantic Search |
| Ollama | Local LLM Runtime |
| Llama 3 | Large Language Model |
| PyPDF | PDF Loader |

---

# 📂 Project Structure

```text
rag-document-qa-bot/
│
├── data/
│   ├── ai.pdf
│   ├── cloud.pdf
│   ├── cybersecurity.pdf
│   └── business.txt
│
├── chroma_db/
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Deepika-Kasaram/Repository-name-rag-document-qa-bot.git

cd Repository-name-rag-document-qa-bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download from

https://ollama.com/download

---

## 5. Download Llama 3

```bash
ollama pull llama3
```

Verify installation

```bash
ollama list
```

Expected output

```
llama3
```

---

# 📥 Add Your Documents

Place your PDF and TXT files inside the **data/** folder.

Example

```
data/
│
├── ai.pdf
├── cloud.pdf
├── cybersecurity.pdf
└── business.txt
```

---

# 📚 Create Vector Database

Run

```bash
python ingest.py
```

Output

```
Loading documents...

Total documents loaded: 4

Total chunks created: 9

Documents indexed successfully!
```

---

# ▶ Run the Application

```bash
python app.py
```

Example

```
Ask a question:

What is Cloud Computing?
```

Answer

```
Cloud computing is the delivery of computing services such as storage,
networking, and servers over the internet.

Common providers include AWS,
Microsoft Azure,
Google Cloud Platform.
```

---

# 🧠 How It Works

```
Documents
      │
      ▼
Text Splitter
      │
      ▼
HuggingFace Embeddings
      │
      ▼
Chroma Vector Database
      │
      ▼
Retriever
      │
      ▼
Ollama (Llama 3)
      │
      ▼
Generated Answer
```

---

# 📦 Requirements

- Python 3.10+
- Ollama
- Llama 3
- LangChain
- ChromaDB
- HuggingFace Embeddings

---

# 📸 Sample Output

```
Ask a question:

What is Cloud Computing?

Answer:

Cloud computing provides computing services such as storage,
networking and servers over the internet.

Major cloud providers include:

• Amazon Web Services (AWS)

• Microsoft Azure

• Google Cloud Platform (GCP)
```

---

# 🎯 Future Improvements

- Streamlit Web UI
- Drag & Drop PDF Upload
- Chat History
- Source Citations
- Multiple Document Collections
- Conversation Memory
- Docker Support
- User Authentication
- Voice Input
- Dark Mode UI

---

# 💡 Learning Outcomes

Through this project, I gained hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- LangChain Pipelines
- Vector Databases
- Semantic Search
- HuggingFace Embeddings
- Ollama
- Local LLM Deployment
- Prompt Engineering
- PDF Processing
- AI Application Development

---

# 👩‍💻 Author

**Deepika Kasaram**

GitHub

https://github.com/Deepika-Kasaram

LinkedIn

https://www.linkedin.com/in/deepika-kasaram/

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork the repository

🤝 Contribute improvements

---

# 📄 License

This project is licensed under the MIT License.
