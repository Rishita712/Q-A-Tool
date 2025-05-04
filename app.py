import streamlit as st
from utils.scraper import scrape_url
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 Web Content Q&A Tool")

url = st.text_input("Enter a webpage URL:")
question = st.text_input("Ask a question:")

if url:
    with st.spinner("Scraping..."):
        scraped = scrape_url(url)
    st.success("Content scraped!")

    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_texts([scraped], embeddings)
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(openai_api_key=openai_key), retriever=vectorstore.as_retriever())

    if question:
        with st.spinner("Thinking..."):
            answer = qa.run(question)
        st.write("💬 **Answer:**", answer)
