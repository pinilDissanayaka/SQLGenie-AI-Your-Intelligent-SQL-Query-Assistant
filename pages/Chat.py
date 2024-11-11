import os
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from database import connect_to_database
from secret import load_secrets
from chat import get_llm_response



st.title("SQLGenie AI Your Intelligent SQL Query Assistant")


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
    
    database_name=st.text_input("Database", value="librarymanagement")
    
    
    if host and port and user and database_name:
        if st.button("Connect to Database"):
            with st.spinner("Connect to the Database:"):
                database=connect_to_database(database_engine=database_engine,host=host, port=int(port), user=user, password=password, database_name=database_name)
                
                if database is not None:
                    if "database" not in st.session_state:
                        st.session_state.database=database
                        
                    st.success("Connected to the Database", icon="✅")
                else:
                    st.error("Failed to connect to the Database", icon="🚫")



if "database" in st.session_state:
    database=st.session_state.database
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
        ]
        
    
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)

    user_query = st.chat_input("Type a message...")
    if user_query is not None and user_query.strip() != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
    
        with st.chat_message("Human"):
            st.markdown(user_query)
        
        with st.chat_message("AI"):
            chat_history = st.session_state.chat_history
            schema = st.session_state.database.get_table_info()
            
            response = get_llm_response(user_query=user_query, schema=schema, chat_history=chat_history)
            
            st.markdown(response)
        
        st.session_state.chat_history.append(AIMessage(content=response))
    
    