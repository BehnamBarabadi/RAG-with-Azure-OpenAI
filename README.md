# RAG-with-Azure-OpenAI
This repository includes the code needed to perform RAG on Azure.

Steps:
1. First we need to create Azure AI Search service:
   Azure AI Search is a vector and full text information retrieval solution for the enterprise, and for traditional and generative AI scenarios.
   Follow this link to create the serivice: https://learn.microsoft.com/en-us/azure/search/search-create-service-portal
   (you need your Admin keys which you can find in Keys section under Settings in your AI Search service.
2. Then run `.ipynb` to create embeddings from the input pdf file and save it.
