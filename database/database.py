from langchain_community.utilities import SQLDatabase


def connect_to_database(database_engine:str, host:str, port:int, user:str, password:str, database_name:str):
    if database_engine == "PostgreSQL":
        return SQLDatabase.from_uri(
            f"postgresql://{user}:{password}@{host}:{port}/{database_name}"
        )
    
    elif database_engine == "Microsoft SQL Server":
        return SQLDatabase.from_uri(
            f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server"
        )
        
    elif database_engine == "MySQL":
        return SQLDatabase.from_uri(
            f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database_name}"
        )