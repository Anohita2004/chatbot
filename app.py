from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you?": "I'm just a bot, but I'm doing great! How about you?",
    "whats the time?": "I'm just a bot and am still under progress and training.",
    "bye": "Goodbye! Have a great day!",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message").lower()
    response = responses.get(user_message, "I didn't understand that. Can you rephrase?")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
