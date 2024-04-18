

import subprocess
import sys
from  backend.biz_azure_ai_search import *
from azure_open_ai.azure_open_ai import *


# from streamlit_chat import message


import streamlit as st


st.title("RAG With Azure AI Search Engine")

st.sidebar.markdown("## Search Engine")

qa_mode = st.sidebar.radio("Question Answering Mode", \
                                 ('Question Answering',
                                  'Chat'))

selected_analysis = st.sidebar.radio("Select the Analysis Type", \
                                 ('Vector Search', 
                                  'Hybrid Search',
                                  'Exhaustive KNN Search',
                                  'Semantic Search'))
st.sidebar.markdown("<hr/>",unsafe_allow_html=True) 


#################################################
llm_output_without_rag = st.sidebar.toggle('Show LLM ouput without RAG')

# if on:
#     st.write('Vector search result')
#################################################


st.sidebar.subheader("Configuration")  

use_langchain = st.sidebar.checkbox("Use Langchain", value=False)

NUMBER_OF_RESULTS_TO_RETURN = st.sidebar.slider("Number of Search Results to Return",\
                                                 1, 10, 3)    


def get_reply(user_input, content):
    """
    user_input is the given prompt by the user
    content is the output of vector search on the provided doc 
    """
    conversation=[{"role": "system",
                   "content": "Assistant is a great language model formed by OpenAI."}]
    reply = generate_reply_from_context(user_input, content, conversation) # this function is in "azure_open_ai.py"
    return reply



def get_details(results_content, results_source):
    st.markdown("### Search result are:")
    for (result,metadata) in zip(results_content,results_source):
        st.write("<html><b>" + 
                 metadata + "</b></html>",
                 unsafe_allow_html=True)
        st.write(result)
        st.write("----")



def get_search_results_azure_aisearch(selected_analysis, user_input):

    """
    This function returns the results from the Azure AI Search Engine

    Returns:
        [results_content,results_source]: 
        Results content and Results Source is returned
    """
    if selected_analysis == 'Vector Search':
       ######################### raw_result is added to the return 
       results_content,results_source = \
       get_results_vector_search(user_input,
                                 NUMBER_OF_RESULTS_TO_RETURN = NUMBER_OF_RESULTS_TO_RETURN)

    elif selected_analysis == 'Hybrid Search':
         
         results_content,results_source = \
            get_results_vector_search(user_input,
            NUMBER_OF_RESULTS_TO_RETURN = NUMBER_OF_RESULTS_TO_RETURN,
            hybrid = True,
            exhaustive_knn=False)

    elif selected_analysis == 'Exhaustive KNN Search':
            results_content,results_source  = \
                get_results_vector_search(user_input,
                NUMBER_OF_RESULTS_TO_RETURN = NUMBER_OF_RESULTS_TO_RETURN,
                hybrid = False,
                exhaustive_knn=True)
            
    elif selected_analysis == 'Semantic Search':
            results_content,results_source  = \
                get_results_vector_search(user_input,
                NUMBER_OF_RESULTS_TO_RETURN = NUMBER_OF_RESULTS_TO_RETURN,
                hybrid = False,
                exhaustive_knn=False,
                semantic_search=True)
                
    return results_content,results_source 



# ##############################################################
#  #   "Question Answering"
# ###############################################################
if qa_mode == "Question Answering" :

    user_input = st.text_input("Enter your question",
                            "What is Segmentation?")
    
    if st.button("Search"):
        ######################### raw_result is added to the return
        results_content, results_source = get_search_results_azure_aisearch(selected_analysis, user_input)
        
        content = "\n".join(results_content)
        # st.write('raw_results:', raw_results)

        if llm_output_without_rag:
            st.markdown("### LLM output without RAG is:")
            reply_azure_openai = get_reply(user_input, content=' ')
            st.write(reply_azure_openai)
            

        st.markdown("<hr/>",unsafe_allow_html=True) 

        if use_langchain == False:
            # get the reply from the LLM
            reply_azure_openai = get_reply(user_input, content)
            # st.markdown("### Answer is:")
            st.write(reply_azure_openai)


        ## get the DETAILS [ CONTENT AND SOURCE ] of the reply from the LLM
        get_details(results_content, results_source)


