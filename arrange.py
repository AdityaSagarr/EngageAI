from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
import uuid
import chromadb

def arrange_dict(page_data,llm):
    prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys:`cname`, `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
    )
    
    chain_extract = prompt_extract | llm 
    res = chain_extract.invoke(input={'page_data': page_data})
    
    json_parser = JsonOutputParser()
    job_data = {k: v for d in json_parser.parse(res.content) for k, v in d.items()}
    
    return job_data