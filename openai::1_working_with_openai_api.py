
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
client = OpenAI(api_key="Enter your key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content": "What is the OpenAPI"}]
)




#activity 3: pass a prompt to the api and get the message.content
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Quick productivity tip."}]
)
# Extract the content from the response
print(response.choices[0].message.content)






#activity 4: calculate the cost 
prompt = f"""Summarise the customer support chat in three concise ket points: {text} """

max_completion_tokens = 500 

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}], 
  max_completion_tokens=max_completion_tokens
)
# Extract the content from the response
print(response.choices[0].message.content)



#activity 5: Calculate the cost 
#define price per token 
input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

input_tokens = response.usage.input_tokens
output_tokens = max_completion_tokens

#Calculate cost 
cost = (input_tokens * input_token_price + output_tokens * output_token_price) 
print(f"Estimated cost: ${cost}")

"""Output: Estimated cost: $0.00124"""
