from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
import uuid
import chromadb

# 2. Database initialization
def db_start():
    # Load CSV and create ChromaDB collection
    df = pd.read_csv(r"C:\Users\Aditya\OneDrive\Desktop\PROFESSIONAL\STUDY\LANGCHAIN\0.PROJECTS\func-mail-project-33\portfolio.csv")
    
    client = chromadb.PersistentClient('vectorstore')
    collection = client.get_or_create_collection(name="portfolio")
    
    if not collection.count():
        for _, row in df.iterrows():
            collection.add(documents=row["Techstack"],
                           metadatas={"links": row["Links"]},
                           ids=[str(uuid.uuid4())])
    
    return collection



def db_fetch(collection, skills):
    links = collection.query(query_texts=skills, n_results=2).get('metadatas', [])
    return links
