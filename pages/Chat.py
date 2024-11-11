import streamlit as st
from database import connect_to_database


st.title("SQLGenie AI Your Intelligent SQL Query Assistant")


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
    
                # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you? 👋"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        try:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = "hi"
                    st.write(response)
                    
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)
        except Exception as e:
            st.warning(f"An unexpected error occurred: {str(e.args)}. Please try again.", icon="⚠️")