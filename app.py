from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fine-tuned model ID
FINETUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal:cryptomarket:AfGQeLb8"

@app.route("/")
def home():
    return "Hello, PTDS class!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        # Use the correct OpenAI method
        response = openai.ChatCompletion.create(
            model=FINETUNED_MODEL,
            messages=[{"role": "user", "content": query}]
        )
        # Access the response correctly
        response_content = response['choices'][0]['message']['content']
        return jsonify({"response": response_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Flask app running with fine-tuned model!")
    app.run(debug=True)