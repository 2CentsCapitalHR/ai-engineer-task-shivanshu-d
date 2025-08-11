import os
from dotenv import load_dotenv
from langchain.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise Exception("Set OPENAI_API_KEY in .env file")

def build_vectorstore(doc_dir="adgm_docs"):
    files = [os.path.join(doc_dir, f) for f in os.listdir(doc_dir) if f.endswith(".docx")]
    documents = []
    for file in files:
        loader = Docx2txtLoader(file)
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def generate_clause_suggestion(missing_item, vectorstore):
    llm = OpenAI(temperature=0)
    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    question = f"Suggest a legally compliant ADGM clause or action for: {missing_item}"
    return qa.run(question)