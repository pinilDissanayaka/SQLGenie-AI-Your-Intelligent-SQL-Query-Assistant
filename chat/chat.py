from llm import get_llm
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Output(BaseModel):
    sql_query: str=Field(description="SQL query for user question")



def get_llm_response(user_query, database, chat_history):
    llm = get_llm().with_structured_output(Output)
    
    
    

    
    