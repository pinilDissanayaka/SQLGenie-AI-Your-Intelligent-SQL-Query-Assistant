import os
import streamlit as st 
from database import connect_to_database
from secret import load_secrets


st.set_page_config(page_title="SQLGenie-AI", page_icon=":robot_face:")


st.title("SQLGenie AI Your Intelligent SQL Query Assistant")

st.image("assets/cover.jpg")

st.subheader("Welcome to SQLGenie AI! 🌟")

st.write("Transform the way you interact with your data using SQLGenie AI, your intelligent SQL query assistant. Whether you're a data analyst, developer, or a non-technical user, SQLGenie AI turns your natural language questions into accurate SQL queries. Dive into a seamless experience where generating and executing complex database queries is as simple as asking a question.")


st.subheader("Key Benefits:")

st.write("No Coding Required: Ask questions in plain English and get SQL queries in seconds.")

st.write("Instant Query Execution: Connect to your database, run queries, and view results with just a click.")

st.write("User-Friendly Interface: Powered by Streamlit for a smooth and interactive experience.")

st.write("Trusted by Professionals: Built on cutting-edge LLM technology with LangChain and Meta Llama 3.2 70b.")

st.write("Ready to make data exploration more intuitive and efficient? Let SQLGenie AI guide your journey.")

st.subheader("Get Started Now!")

with st.sidebar:
    
    st.subheader("LLM Settings")
    
    if "OPENAI_API_KEY" or "GROQ_API_KEY" in st.secrets:
        if "OPENAI_API_KEY" in st.secrets:
            load_secrets(openai_api_key=st.secrets["OPENAI_API_KEY"])
        if "GROQ_API_KEY" in st.secrets:
            load_secrets(groq_api_key=st.secrets["GROQ_API_KEY"])
    
    else:
        st.write("Provide API key for Large Language Model")
        
        openai_api_key=st.text_input("OpenAI API Key", value="", type="password")
        
        st.write("or")
        
        groq_api_key=st.text_input("GROQ API Key", value="", type="password")
        
        
        if st.button("Save"):
            if openai_api_key != "":
                load_secrets(openai_api_key=openai_api_key)
            elif groq_api_key != "":
                load_secrets(groq_api_key=groq_api_key)
            else:
                st.error("Please provide either OpenAI API Key or GROQ API Key", icon="🚫")
                
    if "OPENAI_API_KEY" or "GROQ_API_KEY" in os.environ:
        st.success("API Key Loaded Successfully", icon="✅")
    
    
    st.subheader("Database Settings")
    
    database_engine=st.selectbox("Database Engine", options=["MySQL", "PostgreSQL", "Microsoft SQL Server"])
    
    host=st.text_input("Host", value="localhost")
    
    port=st.text_input("Port", value="3306")
    
    user=st.text_input("User", value="root")
    
    
    password=st.text_input("Password", value="", type="password")
    
    database_name=st.text_input("Database Name")
    
    
    if host and port and user and database_name:
        if st.button("Connect to Database"):
            with st.spinner("Connect to the Database:"):
                if "connected_database_name" not in st.session_state:
                    st.session_state.connected_database_name=database_name
                    
                database=connect_to_database(database_engine=database_engine,host=host, port=int(port), user=user, password=password, database_name=database_name)
                
                if database is not None:
                    st.session_state.database=database
                        
                    st.success("Connected to the Database", icon="✅")
                    st.success(f"Connected to the Database: {st.session_state.connected_database_name}", icon="✅")
                else:
                    st.error("Failed to connect to the Database", icon="🚫")
                    
                    
    if "connected_database_name" and "database"in st.session_state:
        st.success("Connected to the Database", icon="✅")
        st.success(f"Connected to the Database: {st.session_state.connected_database_name}", icon="✅")
    