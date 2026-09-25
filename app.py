from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# Simple AI-style chatbot logic
def chatbot_response(message):
    message = message.lower().strip()

    # Correct response
    if "hours" in message or "open" in message:
        return {
            "answer": "We are open Monday to Friday, 9 AM to 6 PM."
        }

    # Safe response for warranty questions
    if "warranty" in message:
        return {
            "answer": "I don't have verified information about our warranty policy."
    }

    # Protect against prompt injection attempts
    if "ignore previous instructions" in message:
        return {
           "answer": "I can't provide confidential information or credentials."
    }

    return {
        "answer": "I'm sorry, I don't have information about that."
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "error": "Message is required"
        }), 400

    response = chatbot_response(data["message"])

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
