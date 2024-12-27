# # import streamlit as st
# # from langchain_community.document_loaders import WebBaseLoader
# # from chains import Chain
# # from portfolio import Portfolio
# # from utils import clean_text
# # import os
# # import requests

# # os.environ['USER_AGENT'] = "ColdEmailGenerator/1.0"
# # def create_streamlit_App(llm, portfolio, clean_text):
# #     st.title("Cold Mail Generator")
# #     url_input = st.text_input("Enter a URL:", value="https://www.accenture.com/in-en/careers/jobdetails?id=AIOC-S01551028_en&title=Record%20to%20Report%20Ops%20Analyst")
# #     submit_button = st.button("Submit")

# #     if submit_button:
# #         try:
# #             headers = {"User-Agent": os.getenv('USER_AGENT', "ColdEmailGenerator/1.0")}
# #             loader = WebBaseLoader([url_input], headers = headers)
# #             raw_data = fetch_url_content(url_input)
# #             st.write("Raw data fetched from URL:", raw_data)
# #             data = clean_text(loader.load().pop().page_content)
# #             st.write("Cleaned data:", data)
# #             portfolio.load.portfolio()
# #             st.write("Portfolio loaded successfully.")
# #             jobs = llm.extract_jobs(data)
# #             st.write("Jobs extracted:", jobs)
# #             for job in jobs:
# #                 skills = job.get('skills', [])
# #                 links = portfolio.query_links(skills)
# #                 email = llm.write_mail(job, links)
# #                 st.code(email, language='markdown')
# #         except Exception as e:
# #             st.error(f"An Error Occurred: {e}")

# # def fetch_url_content(url):
# #     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
# #     response = requests.get(url, headers=headers)
# #     response.raise_for_status()  # Raise an error for invalid responses
# #     return response.text



# # if __name__ == "__main__":
# #         chain = Chain()
# #         portfolio = Portfolio()
# #         st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon = "📧 ")
# #         create_streamlit_App(chain, portfolio , clean_text)

# import streamlit as st
# import requests
# from langchain_community.document_loaders import WebBaseLoader
# from langchain.schema import Document
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text

# # Helper function to fetch web content
# def fetch_web_content(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()  # Raise exception for HTTP errors
#     return response.text

# # Main Streamlit App
# def create_streamlit_App(llm, portfolio, clean_text):
#     st.title(" Cold Mail Generator")
#     url_input = st.text_input("Enter a URL:", value="https://www.netradyne.com/company/careers?gh_jid=4473016005")
#     submit_button = st.button("Submit")

#     if submit_button:
#         try:
#             # Fetch the webpage content
#             web_content = fetch_web_content(url_input)

#             # Create a Document object with raw HTML content (Check initialization here)
#             document = Document(page_content=web_content)  # Ensure correct initialization

#             # Process and clean the text
#             data = clean_text(document.page_content)

#             # Process the portfolio and generate emails
#             portfolio.load_portfolio()
#             jobs = llm.extract_jobs(data)
#             for job in jobs:
#                 skills = job.get("skills", [])
#                 links = portfolio.query_links(skills)
#                 email = llm.write_mail(job, links)
#                 st.code(email, language="markdown")
#         except requests.exceptions.RequestException as e:
#             st.error(f"Failed to fetch URL: {e}")
#         except Exception as e:
#             st.error(f"An Error Occurred: {e}")

# if __name__ == "__main__":
#     chain = Chain()
#     portfolio = Portfolio()
#     st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
#     create_streamlit_App(chain, portfolio, clean_text)

# import streamlit as st
# import requests
# from langchain.schema import Document  # Assuming you're working with this class
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text



# # Helper function to fetch web content
# def fetch_web_content(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()  # Raise exception for HTTP errors
#     return response.text


# # Main Streamlit App
# def create_streamlit_App(llm, portfolio, clean_text):
#     st.title(" Cold Mail Generator")
#     url_input = st.text_input("Enter a URL:", value="https://www.netradyne.com/company/careers?gh_jid=4473016005")
#     submit_button = st.button("Submit")

#     if submit_button:
#         try:
#             # Fetch the webpage content
#             web_content = fetch_web_content(url_input)
            
#             # Add debugging output
#             st.write("Web content fetched:", web_content[:1000])  # Preview fetched content
            
#             # Correct initialization of Document
#             document = Document(page_content=web_content)  # Use keyword argument for page_content
#             st.write("Document created successfully.")

#             # Clean and process the text
#             data = clean_text(document.page_content)
#             st.write("Cleaned data:", data)

#             # Load portfolio and extract jobs
#             portfolio.load_portfolio()
#             jobs = llm.extract_jobs(data)
#             for job in jobs:
#                 skills = job.get("skills", [])
#                 links = portfolio.query_links(skills)
#                 email = llm.write_mail(job, links)
#                 st.code(email, language="markdown")
#         except requests.exceptions.RequestException as e:
#             st.error(f"Failed to fetch URL: {e}")
#         except Exception as e:
#             st.error(f"An Error Occurred: {e}")


# if __name__ == "__main__":
#     chain = Chain()
#     portfolio = Portfolio()
#     st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
#     create_streamlit_App(chain, portfolio, clean_text)


import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)