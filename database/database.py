from langchain_community.utilities import SQLDatabase


def connect_to_database(host:str, port:int, user:str, password:str, database_name:str):
    return SQLDatabase.from_uri(
        f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database_name}"
    )