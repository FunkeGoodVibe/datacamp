
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
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")
"""Output: Estimated cost: $0.00124"""


#activity 6: controlling randomness in the response
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
    temperature=2 #0=deterministic, 2=more random
)
print(response.choices[0].message.content)
#response.choices[0].messages.content 


#activity 7: chat roles 
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system",
            "content": "You are a python programming tutor who speaking consisely."},
              {"role": "user", 
            "content": "What is the difference between mutable and ?"}]
)
print(response.choices[0].message.content)


sys_msg = """
    You are finance education assistnat that helps students study for exams.

    If you are asked for specific, real-world financial advice with risk to their finances, response with:

    I'm sorry, I am not allowed to provide financial advice
"""


#activity 8: assistan 
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)


#activity 9: coding a conversation 
messages = [{"role: system", 
            "content": "You are a data science tutor who provides short, simple explanations."}]

user_qs = ["Why is Python so popular?"]

for q in user_qs: 

    user_dict = {"role":"user", "content": q}
    messages.append(user_dict)

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages
    )

    assistant_dict = {"role":"assistant", "content":response.choices[0].message.content}
    messages.append(assistant_dict)