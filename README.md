# RAG-with-Azure-OpenAI
This repository includes the code needed to perform RAG on Azure.

## **Steps:**
### 1. Create embeddings:
   Run `.ipynb` to create embeddings from the input pdf file and save it on your local machine.
### 2. Create Azure AI Search service:
   Azure AI Search is a vector and full text information retrieval solution for the enterprise, and for traditional and generative AI scenarios.
   Follow this link to create the serivice: https://learn.microsoft.com/en-us/azure/search/search-create-service-portal
   (you need your Admin keys which you can find in Keys section under Settings in your AI Search service and also the endpoint URL which in under Overview.
### 3. Create search index in Azure:
   Run `.ipynb` file to create search index in Azure and upload the documents to it. Then go to your search service on Azure check Index, you should see your search index there with your given name    and inside it you will see all the uploaded documents(chunks)
### 4. Perform AI search
   Run `3.azure_ai_vector_search.ipynb` file to do a vector search on the uploaded files with a given query
   
### 5. Create a virtual environment and run `main.py`
   look at `Steps to create virtual environmen.txt` file and follow the steps to create a virtual environment and then run the `app.py` file using `streamlit app.py` command
   
The UI that is used to interact with the code is Streamlit.
