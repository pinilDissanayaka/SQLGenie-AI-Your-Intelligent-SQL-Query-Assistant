import os
import streamlit as st 
from langchain_groq.chat_models import ChatGroq
from langchain_openai.chat_models import ChatOpenAI




def get_llm():
    if "OPENAI_API_KEY" in os.environ:
        return ChatOpenAI(temperature=0)
    elif "GROQ_API_KEY" in os.environ:
        return ChatGroq(model="llama-3.1-70b-versatile", temperature=0)
    else:
        st.error("Please provide either OpenAI API Key or GROQ API Key", icon="🚫")