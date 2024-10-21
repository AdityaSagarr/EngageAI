from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
import uuid
import chromadb

# Function to scrape the page content from the job link
def scrape(job_link):
    loader = WebBaseLoader(job_link)
    page_data = loader.load().pop().page_content
    return page_data

