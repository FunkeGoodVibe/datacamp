
## 

#activity 1: pass a prompt to the api
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
  
    # Enter your prompt
    messages=[{"role": "user", "content": "what is the purpose of an api"}]
)

print(response.choices[0].message.content)


#activity2 : pass a prompt to the api and specify the number of tokens in the response
from openai import OpenAI 
client - OpenAI(api_key="Enter your key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content": "What is the OpenAPI"}]
)



