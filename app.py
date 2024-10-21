import streamlit as st
from scraper import scrape
from arrange import arrange_dict
from database import db_start, db_fetch
from email_generator import generate_mail
from langchain_groq import ChatGroq

# Initialize the ChatGroq model
llm = ChatGroq(
    model="llama-3.2-90b-vision-preview", # U CAN CHOOSE OTHER MODELS
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    groq_api_key='your_groq_api_key'
)

def main():
    # Set the layout to wide
    st.set_page_config(layout="wide")

    # Custom CSS for left alignment and code area size
    st.markdown("""
        <style>
            .stApp {
                text-align: left;
            }
            .stCode {
                width: 100%;  /* Adjust width as needed */
                font-size: 16px; /* Adjust font size */
                padding: 10px;  /* Add padding for better appearance */
                border: 1px solid #e1e1e1; /* Optional border */
                background-color: #f7f7f7; /* Optional background color */
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("🤝 EngageAI")  # Added emoji to the title
    st.header("📧 Automating Client Outreach")  # Added emoji to the header
    
    job_link = st.text_input("Enter Job Link:")
    
    if st.button("Generate Email"):
        # Step 1: Scrape job page content
        page_content = scrape(job_link)
        
        if len(page_content) > 50:
            # Step 2: Process the scraped content to get job details
            job_data = arrange_dict(page_content, llm)  # Pass llm to the function

            # Step 3: Initialize the database
            collection = db_start()

            # Step 4: Fetch relevant portfolio links
            fetched_links = db_fetch(collection, job_data['skills'])

            # Step 5: Generate email using the job data and fetched links
            email_output = generate_mail(job_data, fetched_links, llm)  # Pass llm to the function

            # Display the generated email output in a markdown format with copy option
            st.markdown("### Generated Email Output")
            st.code(email_output, language="text")  # Removed line_height argument
            st.markdown("You can copy the email text above.")
        else:
            st.markdown("Website has restricted from reading")
            

if __name__ == "__main__":
    main()
