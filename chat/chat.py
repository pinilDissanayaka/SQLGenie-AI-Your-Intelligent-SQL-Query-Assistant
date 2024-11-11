from llm import get_llm
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from prompts import few_short_prompt_template, structured_prompt_template


class Output(BaseModel):
    sql_query: str=Field(description="SQL query for user question")



def get_llm_response(user_query, schema, chat_history):
    llm = get_llm().with_structured_output(Output)
    
    prompt=ChatPromptTemplate.from_template(structured_prompt_template)
    
    
    chat_chain=(
        {"QUESTION": RunnablePassthrough(), "SCHEMA": schema, "CHAT_HISTORY": chat_history} |
        prompt |
        llm
    )
    
    return chat_chain.invoke(user_query)
    

    
    