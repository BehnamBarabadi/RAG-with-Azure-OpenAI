# **Retrieval Augmented Generation (RAG) in Azure AI SearchI**
- https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
  
Retrieval Augmented Generation (RAG) is an architecture that augments the capabilities of a Large Language Model (LLM) like ChatGPT by adding an information retrieval system that provides grounding data. Adding an information retrieval system gives you control over grounding data used by an LLM when it formulates a response.

Custom RAG pattern for Azure AI Search
A high-level summary of the pattern looks like this:

Start with a user question or request (prompt).
Send it to Azure AI Search to find relevant information.
Send the top ranked search results to the LLM.
Use the natural language understanding and reasoning capabilities of the LLM to generate a response to the initial prompt.
Azure AI Search provides inputs to the LLM prompt, but doesn't train the model. In RAG architecture, there's no extra training. The LLM is pretrained using public data, but it generates responses that are augmented by information from the retriever.

RAG patterns that include Azure AI Search have the elements indicated in the following illustration.
![architecture-diagram](https://github.com/BehnamBarabadi/RAG-with-Azure-OpenAI/assets/59636426/9bc99705-296d-43df-bea0-156504315d39)

- App UX (web app) for the user experience
- App server or orchestrator (integration and coordination layer)
- Azure AI Search (information retrieval system)
- Azure OpenAI (LLM for generative AI)

The web app provides the user experience, providing the presentation, context, and user interaction. Questions or prompts from a user start here. Inputs pass through the integration layer, going first to information retrieval to get the search results, but also go to the LLM to set the context and intent.


**This repository includes the code needed to perform RAG on Azure.**

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
   First you need to create a `Azure OpenAI` service, then follow the steps in `Steps to create virtual environmen.txt` file to create a virtual environment and run the `app.py` file using `streamlit app.py` command
   - https://www.codecademy.com/article/getting-started-with-azure-open-ai-service
     
  The UI that is used to interact with the code is Streamlit.
