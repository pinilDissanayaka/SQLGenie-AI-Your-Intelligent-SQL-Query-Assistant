# SQLGenie-AI-Your-Intelligent-SQL-Query-Assistant 🧞‍♂️



SQLGenie AI is an intelligent assistant designed to bridge the gap between natural language and SQL queries. This project enables users to generate SQL queries from natural language prompts using powerful Large Language Models (LLMs). Users can interact with the app through a simple web interface built with Streamlit and can choose between OpenAI GPT and Meta LLaMA 3.2 70B models for query generation.

![Screenshot 2024-11-12 000009](https://github.com/user-attachments/assets/1197fcab-1daf-4b7f-85c0-d0631f426cbc)
![Screenshot 2024-11-11 235350](https://github.com/user-attachments/assets/1900f35b-3fe9-4786-9edb-6eafc5c5ad7a)
![Screenshot 2024-11-11 235628](https://github.com/user-attachments/assets/818ad737-1cee-405f-aadc-1cde7f45bf95)


## Features
- Natural Language to SQL Query Conversion: Easily transform plain English questions into valid SQL queries.
- Choose Your LLM: Select between OpenAI GPT or Meta LLaMA 3.2 70B model for different performance options.
- Interactive Web Interface: A user-friendly interface powered by Streamlit for seamless interaction.
- Query Execution: Run generated SQL queries directly on a connected database and display the results.
- Error Handling & Explanations: Get feedback for any issues in query execution and explanations for generated SQL code.

## Tech Stack
LangChain: Used for managing LLM interactions and prompt engineering.
OpenAI GPT: For generating SQL queries from natural language input.
Meta LLaMA 3.2 70B: As an alternative LLM for generating queries.
Streamlit: Provides an interactive web interface.
Database: MySQL (default) – expandable to support PostgreSQL, Microsoft SQL Server, etc.
sqlalchemy for database connectivity.

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/sqlgenie-ai.git
cd sqlgenie-ai
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the Streamlit app:
```
streamlit run app.py
```

## Usage
- Open the app in your web browser (usually runs on http://localhost:8501).
- Enter your natural language question in the input box.
- Select the LLM model (OpenAI GPT or Meta LLaMA 3.2 70B) from the dropdown menu.
- Click Generate SQL to see the generated SQL query.
- Optionally, click Run Query to execute the SQL query on the connected database and display the results.

## Configuration
- Database Setup: By default, the app uses MySQL. To connect to other databases (e.g., PostgreSQL, Microsoft SQL Server), modify the connection string in the execute_sql_query function.
- Model Selection: Ensure that you have access to both LLMs and their required configurations for smooth operation.

## Contributing

We welcome contributions! If you'd like to add new features, fix bugs, or enhance performance:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Commit your changes (git commit -m 'Add a new feature').
4. Push to the branch (git push origin feature/your-feature-name).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, please open an issue on this repository.
