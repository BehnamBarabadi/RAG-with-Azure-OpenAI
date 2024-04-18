# RAG-with-Azure-OpenAI
This repository includes the code needed to perform RAG on Azure.

## **Steps:**
### 1. Create embeddings:
   Run `.ipynb` to create embeddings from the input pdf file and save it on your local machine.
### 2. Create Azure AI Search service:
   Azure AI Search is a vector and full text information retrieval solution for the enterprise, and for traditional and generative AI scenarios.
   Follow this link to create the serivice: https://learn.microsoft.com/en-us/azure/search/search-create-service-portal
   (you need your Admin keys which you can find in Keys section under Settings in your AI Search service and also the endpoint URL which in under       Overview.
### 3. Create search index in Azure:
   Run `.ipynb` file to create search index in Azure and upload the documents to it
   
