import streamlit as st 
from database import connect_to_database


st.set_page_config(page_title="SQLGenie-AI", page_icon=":robot_face:")


st.title("SQLGenie-AI-Your-Intelligent-SQL-Query-Assistant")

st.image("assets/cover.jpg")

with st.sidebar:

    st.subheader("Database Settings")
    
    host=st.text_input("Host", value="localhost")
    
    port=st.text_input("Port", value="3306")
    
    user=st.text_input("User", value="root")
    
    password=st.text_input("Password", value="", type="password")
    
    database_name=st.text_input("Database", value="librarymanagement")
    
    
    if host and port and user and database_name:
        if st.button("Connect to Database"):
            with st.spinner("Connect to the Database:"):
                database=connect_to_database(host=host, port=int(port), user=user, password=password, database_name=database_name)
                
                if database is not None:
                    st.success("Connected to the Database", icon="✅")
                else:
                    st.error("Failed to connect to the Database", icon="🚫")
