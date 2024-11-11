import os
import streamlit as st 
from langchain_groq.chat_models import ChatGroq
from langchain_openai.chat_models import ChatOpenAI




def get_llm():
    if "OPENAI_API_KEY" in os.environ:
        return ChatOpenAI(temperature=0.8)
    elif "GROQ_API_KEY" in os.environ:
        return ChatGroq(temperature=0.8)
    else:
        st.error("Please provide either OpenAI API Key or GROQ API Key", icon="🚫")