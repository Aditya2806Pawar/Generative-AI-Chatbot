"""
Author: Aditya2806Pawar
https://github.com/Aditya2806Pawar
"""

class Config:
    PAGE_TITLE = "Genrative AI Chatbot"

    OLLAMA_MODELS = ( 'mistral:latest','codellama:latest')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic."""
    