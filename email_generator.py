from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
import uuid
import chromadb

# 4. Generate email using LLM
def generate_mail(job, links, llm):
    prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Aditya, a business development executive at SynergySoft. SynergySoft is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. Also, mention the job role in the subject for which you are writing this mail.
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above, describing the capability of SynergySoft 
        in fulfilling their needs.
        also after around 24 words add change line to the response
        Also, add the most relevant ones from the following links to showcase SynergySoft's portfolio: {link_list}
        Remember you are Aditya, BDE at SynergySoft. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
    )
    
    chain_email = prompt_email | llm
    res = chain_email.invoke({"job_description": str(job), "link_list": links})
    
    return res.content

