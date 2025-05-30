# crypto_advisor_bot.py

# 👋 Intro message
print("\U0001F44B Hi, I’m CryptoBuddy—your friendly AI crypto sidekick!")
print("Let’s find you a green and growing coin! \U0001F680\U0001F331")

# Predefined crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Chatbot logic
def chatbot_response(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"\u2705 {recommend} is the most sustainable! \U0001F33F It’s eco-friendly and has long-term potential."

    elif "trending" in user_query or "rising" in user_query:
        rising_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"\U0001F4C8 These coins are trending up: {', '.join(rising_coins)}."

    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"\U0001F680 {name} is trending up and has a top-tier sustainability score! Great for long-term growth."

    elif "most profitable" in user_query or "best return" in user_query:
        profitable = [name for name, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        return f"\U0001F4B0 These coins are likely to be profitable: {', '.join(profitable)}."

    else:
        return "\U0001F914 I’m still learning! Try asking about sustainable or trending cryptos."

# Chat loop
while True:
    user_query = input("\nYou: ")
    if user_query.lower() in ['exit', 'quit']:
        print("CryptoBuddy: Goodbye! \U0001F6AA")
        break
    print("CryptoBuddy:", chatbot_response(user_query))

# Disclaimer
print("\n\u26A0\uFE0F Crypto is risky—always do your own research before investing!")
