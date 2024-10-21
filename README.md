

---

# 🚀 EngageAI: Automating Client Outreach 🤖

## Overview

EngageAI is an innovative project designed to streamline the client outreach process for job applications using advanced AI technologies. This project harnesses the power of the open-source **Llama 3.1 LLM**, integrated with **ChromaDB**, **LangChain**, and **Streamlit**, to facilitate cold emailing strategies for software service companies targeting potential clients like **Nike** and **JP Morgan**.

## Problem Statement

In a highly competitive landscape, sales teams at software service companies such as **TCS**, **Infosys**, **Accenture**, and **Cognizant** often seek to connect with potential clients by identifying job postings on client portals. For instance, when a client like **Nike** posts a requirement for a software engineer with expertise in **AI/ML**, sales representatives need to craft compelling emails that effectively showcase their capabilities to fulfill those specific needs.

## How It Works

1. **Job Portal Scraping**: The system scrapes job postings to extract relevant skills and descriptions.
2. **LLM-Powered Email Generation**: EngageAI utilizes **Llama 3.1** to analyze job requirements and generate personalized cold emails tailored to the client's needs.
3. **Portfolio Matching**: By integrating with **ChromaDB**, the tool retrieves relevant portfolio links that highlight past projects aligned with the required skills.

## Technical Architecture

- **LangChain**: Used for data extraction from job postings.
- **Llama 3.1/OpenAI LLM**: Generates customized emails based on job descriptions.
- **ChromaDB**: A vector database for storing and retrieving skill-specific portfolios.

## Project Files

- `vectorstore/`: Contains the vector database for storing skill-specific portfolios.
- `TEST.ipynb`: A Jupyter notebook for testing various functionalities.
- `app.py`: The main application file built with Streamlit.
- `arrange.py`: Contains the logic for processing and arranging scraped data.
- `database.py`: Handles database initialization and queries.
- `email_generator.py`: Generates personalized emails based on job data and portfolio links.
- `portfolio.csv`: A CSV file containing the portfolio data.
- `scraper.py`: Implements web scraping to extract job postings.
- `requirements.txt`: Lists the project dependencies.

## Installation

To get started with EngageAI, clone the repository and install the required packages:

```bash
git clone https://github.com/AdityaSagarr/EngageAI.git
cd EngageAI
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Enter a job link in the provided input field and click **"Generate Email."**

3. The generated email output will be displayed for copying.

### 📸 Project Screenshot
![tuxpi com 1729520032](https://github.com/user-attachments/assets/6682c959-05a4-46c4-8c0c-93394bfd098b)

### 🔧 Note

* Don’t forget to update model-related specifications in `app.py` to ensure optimal performance!
* This project assumes that you are Aditya, a business development executive at SynergySoft,which can be adapted for different consulting firms, allowing it to scale based on their unique business development strategies and client requirements


## Adaptability

EngageAI is designed to be adaptable for various consulting firms, enabling scalability based on unique business development strategies and client requirements. This tool not only enhances the efficiency of email outreach but also significantly increases the chances of client engagement.

## Feedback and Contributions

I welcome any feedback or discussions regarding the project. Feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/adityasagarr)!

## Acknowledgements

Thank you for exploring EngageAI! Together, we can innovate and transform client engagement strategies through automation and AI.

---



