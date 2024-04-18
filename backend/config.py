from dotenv import load_dotenv, dotenv_values, find_dotenv
import os

# Configure environment variables  
load_dotenv(dotenv_path=r'C:\Users\Seyed Barabadi\Downloads\Gen AI\AZURE-AI-VECTOR-SEARCH-main\azure_ai_vector_search\backend\azure_keys.env') 
# load_dotenv(find_dotenv())  

# Azure AI Search
AZURE_SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT") 
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME") 
AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME")
AZURE_SEARCH_SEMANTIC_CONFIG_NAME = os.getenv("AZURE_SEARCH_SEMANTIC_CONFIG_NAME")

NUMBER_OF_RESULTS_TO_RETURN = os.getenv("NUMBER_OF_RESULTS_TO_RETURN")
NUMBER_OF_NEAR_NEIGHBORS = os.getenv("NUMBER_OF_NEAR_NEIGHBORS")

# Azure OpenAI
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_ID = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID")
AZURE_OPENAI_DEPLOYMENT_ID_AGENTS = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID_AGENTS")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_ID = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_ID")





