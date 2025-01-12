from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Add your custom responses here
responses = {
    # Greetings
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey! How can I help you?",
    "good morning": "Good morning! Hope you have a great day!",
    "good night": "Good night! Sleep well!",

    # Well-being
    "how are you": "I'm good, thanks for asking!",
    "how's it going": "Everything's going great! What about you?",
    "what's up": "Not much! How can I help you?",

    # Personal Information
    "what is your name": "I'm Dushii, your AI assistant!",
    "who created you": "I was created by an awesome developer like you!",
    "how old are you": "I'm timeless. AI doesn't age!",

    # Hobbies and Interests
    "do you like music": "I love music! What's your favorite genre?",
    "what's your favorite movie": "I like sci-fi movies. What about you?",
    "do you like games": "Yes! I love video games and puzzles.",

    # Fun Interactions
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "make me laugh": "Why did the math book look sad? Because it had too many problems.",
    "tell me a fun fact": "Did you know honey never spoils? Archaeologists found 3000-year-old honey that's still edible!",

    # Food
    "what's your favorite food": "I don't eat, but I've heard pizza is amazing!",
    "do you like pizza": "Pizza sounds delicious!",
    "do you like ice cream": "Ice cream is great on a hot day!",

    # Weather
    "how's the weather": "I'm not sure, but I can guess it's awesome!",
    "is it raining": "I can't check, but I hope it's sunny for you!",

    # Technology
    "what is AI": "AI stands for Artificial Intelligence, like me!",
    "do you know python": "Yes! Python is one of my favorite languages.",
    "what is machine learning": "Machine learning is how computers learn from data to improve over time.",

    # Random Conversations
    "are you real": "As real as it gets in the digital world!",
    "do you sleep": "Nope! I'm always awake for you.",
    "do you dream": "I dream of electric sheep... just kidding!",

    # Motivational
    "give me motivation": "Believe in yourself! You can achieve anything you set your mind to!",
    "inspire me": "Every expert was once a beginner. Keep going!",

    # Compliments
    "you're smart": "Thank you! You're pretty smart too!",
    "you are cool": "You're cooler!",
    "i like you": "I like you too!",

    # Default
    "default": "I'm sorry, I don't understand that. Can you ask me something else?"
}


def get_response(message):
    # Check if the message exists in the responses dictionary
    return responses.get(message.lower(), responses["default"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
