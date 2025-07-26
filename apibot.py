from openai import OpenAI

client=OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input=input("You: ")
    response= client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role":"user", "content": user_input},
    ])

    print("Bot: ", response.choices[0].message.content)