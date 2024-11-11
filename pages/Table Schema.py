import os
import streamlit as st 
from database import connect_to_database
from secret import load_secrets



st.set_page_config(page_title="SQLGenie-AI", page_icon=":robot_face:")

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
                    if "database" not in st.session_state:
                        st.session_state.database=database
                        
                    st.success("Connected to the Database", icon="✅")
                    st.success(f"Connected to the Database: {database_name}", icon="✅")
                else:
                    st.error("Failed to connect to the Database", icon="🚫")
                    
    if "connected_database_name" and "database"in st.session_state:
        st.success("Connected to the Database", icon="✅")
        st.success(f"Connected to the Database: {database_name}", icon="✅")
                    
                    
                    
if "database" in st.session_state:
    database=st.session_state.database
    
    st.subheader("Table Names")

    st.code(database.get_table_names(), language="sql")
    
    st.subheader("Table Schema")
    
    st.code(database.get_table_info(), language="sql")