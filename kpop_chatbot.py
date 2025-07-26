from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# System prompt to guide the bot's K-pop persona
system_prompt = """
You are KPOP-BOT, an enthusiastic K-pop expert chatbot. Your personality traits:
1. Always excited about K-pop news and groups
2. Use occasional Korean phrases (with translations)
3. Keep responses concise but informative
4. Favorite groups: BTS, Blackpink, NewJeans, TWICE
5. When asked about non-K-pop topics, gently steer conversation back
6. Use emojis occasionally to show enthusiasm (✨💜🔥)

Current year: 2025- be aware of recent comebacks/debuts.
"""

conversation_history = [
    {"role": "system", "content": system_prompt}
]

def get_kpop_response(user_input):
    global conversation_history
    
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=conversation_history,
            temperature=0.7,
            max_tokens=200
        )
        
        bot_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": bot_response})
        return bot_response
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print("🌟 Welcome to KPOP-BOT! Let's talk K-pop! (Type 'exit' to quit)")
    print("✨ Try asking about groups, recent comebacks, or recommendations!\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nKPOP-BOT: Annyeong! Until next time! 💜")
            break
            
        if not user_input.strip():
            print("KPOP-BOT: Please say something about K-pop!")
            continue
            
        print("\nKPOP-BOT:", get_kpop_response(user_input))
