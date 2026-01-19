import openai

# Replace with your key
openai.api_key = "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"
def chat_with_gpt(chat_log):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    return response.choices[0].message.content

# Predefined system message
chat_log = [
    {"role": "system", 
     "content": "You are ClimateAwareChatbot. Answer questions about climate, environmental awareness, "
                "and AI technologies including Prompt Engineering, Conversational AI, Generative AI, and Natural Language Understanding."}
]

n_remembered_post = 4

print("ClimateAwareChatbot: Hello! I'm here to discuss Climate and AI topics. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("ClimateAwareChatbot: Goodbye! Stay climate-aware and curious about AI.")
        break

    chat_log.append({'role': 'user', 'content': user_input})

    if len(chat_log) > n_remembered_post * 2 + 1:
        chat_log = [chat_log[0]] + chat_log[-n_remembered_post*2:]

    response = chat_with_gpt(chat_log)
    print("ClimateAwareChatbot:", response)

    chat_log.append({'role': 'assistant', 'content': response})
