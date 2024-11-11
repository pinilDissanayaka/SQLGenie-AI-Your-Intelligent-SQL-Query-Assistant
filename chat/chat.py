from llm import get_llm
from langchain_core.runnables import RunnablePassthrough   
from langchain_core.output_parsers import StrOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from prompts import few_short_prompt_template, structured_prompt_template, natural_language_prompt_template


class Output(BaseModel):
    sql_query: str=Field(description="SQL query for user question")



def get_sql_query_from_llm(user_query, schema, chat_history):
    llm = get_llm().with_structured_output(Output)
    
    prompt=ChatPromptTemplate.from_template(structured_prompt_template)
    
    
    chat_chain=(
        {"QUESTION": RunnablePassthrough(), "SCHEMA": RunnablePassthrough(), "CHAT_HISTORY": RunnablePassthrough()} |
        prompt |
        llm
    )
    
    output= chat_chain.invoke({"QUESTION": user_query, "SCHEMA": schema, "CHAT_HISTORY": chat_history})
    
    return output.sql_query
    


def get_llm_response(user_query, database, chat_history):
    llm=get_llm()
    schema=database.get_table_info()
    
    prompt=ChatPromptTemplate.from_template(natural_language_prompt_template)
    
    chat_chain=(
        {"QUESTION": RunnablePassthrough(), "SQL_RESPONSE": RunnablePassthrough(), "QUERY": RunnablePassthrough()} 
        | prompt 
        | llm 
        | StrOutputParser()
    )
    
    sql_query=get_sql_query_from_llm(user_query=user_query, schema=schema, chat_history=chat_history)
    
    sql_response=database.run(sql_query)
    
    
    return chat_chain.invoke({"QUESTION": user_query, "CHAT_HISTORY": chat_history, "QUERY": sql_query})