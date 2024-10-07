import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    # Updated UI with a modern and interactive design
    st.title("📬 Smart Cold Outreach Companion")
    st.subheader("Automate Your Job Applications with AI-Powered Cold Emails")

    # Enhanced user input section
    st.write("💼 **Enter the URL of the job listing you'd like to apply for:**")
    url_input = st.text_input("Job URL", value="https://www.uber.com/global/en/careers/list/133792/", placeholder="Paste the job URL here")
    
    st.write("✉️ **Get a tailored cold email with matching skills and portfolio links!**")
    submit_button = st.button("Generate Cold Email")

    if submit_button:
        with st.spinner('Fetching job details and generating email...'):
            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)
                    st.success("Cold Email Generated Successfully!")
                    st.code(email, language='markdown')
            except Exception as e:
                st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Smart Cold Outreach Companion", page_icon="📬")
    create_streamlit_app(chain, portfolio, clean_text)
