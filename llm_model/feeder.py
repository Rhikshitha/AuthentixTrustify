from dotenv import load_dotenv
import os

# from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_and_split_docs(chunk_size=1024, chunk_overlap=100):
    loader = TextLoader(
        "docs/sample.txt"
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunks = loader.load_and_split(text_splitter=text_splitter)
    return chunks

def main():
    load_dotenv()
    token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    chunks = load_and_split_docs()
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vector_store = FAISS.from_documents(documents = chunks, embedding = embeddings)
    vector_store.save_local("faiss_vector_db")
    
    print("completed feeding")

if __name__ == "__main__":
    main()
