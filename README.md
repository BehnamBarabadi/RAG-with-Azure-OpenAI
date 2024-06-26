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
### 1. Create Embeddings::
   Run `1.create_embeddings.ipynb` to generate embeddings from the input PDF file and save them on your local machine..
### 2. Create Azure AI Search Service::
   Azure AI Search is a solution for vector and full-text information retrieval, suitable for enterprise and various AI scenarios. Follow [Create an Azure AI Search service in the portal](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal) to create the service. You will need your Admin keys (found in the Keys section under Settings in your AI Search service) and the endpoint URL (found under Overview).
### 3. Create search index in Azure:
   Run `.ipynb` file to create search index in Azure and upload the documents to it. Then go to your search service on Azure check Index, you should see your search index there with your given name    and inside it you will see all the uploaded documents(chunks)
### 4. Perform AI search
   Run `3.azure_ai_vector_search.ipynb` file to conduct a vector search on the uploaded files with a provided query.
### 5. Create a virtual environment and run `main.py`
  Firstly, create an `Azure OpenAI` service. Then, follow the steps outlined in the "Steps to Create Virtual Environment.txt" file to set up a virtual environment. Finally, execute the app.py file using the command `streamlit app.py`. Refer to [getting-started-with-azure-open-ai-service](https://www.codecademy.com/article/getting-started-with-azure-open-ai-service) for guidance on setting up the Azure OpenAI service. The user interface utilized to interact with the code is Streamlit. For more information, visit the [Streamlit documentation](https://docs.streamlit.io/get-started).
  
