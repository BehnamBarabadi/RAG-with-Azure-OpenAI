from backend.config import *
from openai import AzureOpenAI



client = AzureOpenAI(
  azure_endpoint = AZURE_OPENAI_ENDPOINT,
  api_key=AZURE_OPENAI_KEY,  
  api_version="2023-05-15"
)


def create_prompt(content, query):
    header = "You are helpful assistant."
    return header + content + "\n\n" + query + "\n"


def generate_answer(conversation):


    response = client.chat.completions.create(
                                            model=AZURE_OPENAI_DEPLOYMENT_ID, # same as deployment name
                                            messages=conversation,
                                            temperature=0,
                                            max_tokens=1000,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            stop = [' END']
                                            )
    return (response.choices[0].message.content).strip()

def generate_reply_from_context(user_input, content, conversation):
    # input: conversation = [{"role": "system", "content": "Assistant is a great language model formed by OpenAI."}]
    prompt = create_prompt(content, user_input)            
    conversation.append({"role": "assistant", "content": prompt})
    conversation.append({"role": "user", "content": user_input})
    reply = generate_answer(conversation)
    return reply