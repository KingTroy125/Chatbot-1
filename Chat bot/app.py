from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def generate_reply(user_message):
    # Basic response logic
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm the ChatBot, your virtual assistant.",
        "bye": "Goodbye! Have a great day!"
    }
    user_message = user_message.lower()
    return responses.get(user_message, "Sorry, I didn't understand that.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_reply = generate_reply(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
