few_short_prompt_template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
    
    <SCHEMA>{SCHEMA}</SCHEMA>
    
    Conversation History: {CHAT_HISTORY}
    
    Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
    
    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;
    
    Your turn:
    
    Question: {QUESTION}
    SQL Query:
"""

structured_prompt_template = """
    Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
    
    <SCHEMA>{SCHEMA}</SCHEMA>
    
    Conversation History: {CHAT_HISTORY}
    
    Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
    
    Question: {QUESTION}
    SQL Query:
"""


natural_language_prompt_template = """
    Based on the table schema below, question, sql query, and sql response, write a natural language response.
    
    SQL Query: <SQL>{QUERY}</SQL>
    
    User question: {QUESTION}
    
    SQL Response: {SQL_RESPONSE}
    
    Write only the natural language response and nothing else. Do not wrap the natural language response in any other text, not even backticks.
"""