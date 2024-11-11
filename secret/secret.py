import os

def load_secrets(groq_api_key=None, openai_api_key=None):
    if groq_api_key is not None:
        os.environ["GROQ_API_KEY"] = groq_api_key

    if openai_api_key is not None:
        os.environ["OPENAI_API_KEY"] = openai_api_key