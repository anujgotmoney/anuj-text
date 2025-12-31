from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# This is the list of 25 unique replies
REPLY_LIST = [
    "Hello there!", "Hi!", "Greetings!", "Salutations!", "Hey!",
    "Howdy!", "What's up?", "Good to see you!", "Yo!", "Hiya!",
    "Welcome!", "Nice to meet you!", "Hey friend!", "Aloha!", "Hola!",
    "Bonjour!", "Guten Tag!", "Namaste!", "Konichiwa!", "Ciao!",
    "Hey hey hey!", "Top of the morning!", "Good day!", "Look who it is!",
    "Greetings and salutations!"
]

@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({"message": "Send a POST request to /reply with {'message': 'hi'}"})

@app.route('/reply', methods=['POST'])
def reply_bot():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Check if user sent a message
        if not data or 'message' not in data:
            return jsonify({"error": "No message provided"}), 400

        user_message = data['message'].lower().strip()

        # If the message is "hi", return the 20+ replies
        if user_message == 'hi':
            return jsonify({
                "status": "success",
                "trigger": "hi",
                "count": len(REPLY_LIST),
                "replies": REPLY_LIST # This sends the array of 20+ messages
            })
        
        else:
            return jsonify({
                "status": "ignored",
                "message": "I only respond to 'hi'"
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel requires the 'app' object to be available
if __name__ == '__main__':
    app.run(debug=True)
    