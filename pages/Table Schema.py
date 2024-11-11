import streamlit as st

import streamlit as st 
from database import connect_to_database


st.set_page_config(page_title="SQLGenie-AI", page_icon=":robot_face:")

with st.sidebar:

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
    
    st.subheader("Table Names")

    st.code(database.get_table_names(), language="sql")
    
    st.subheader("Table Schema")
    
    st.code(database.get_table_info(), language="sql")