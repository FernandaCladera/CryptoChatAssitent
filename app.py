from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__,template_folder="templates")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FINETUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal:cryptomarket:AfGQeLb8"

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        response = client.chat.completions.create(
            model=FINETUNED_MODEL,
            messages=[{"role": "user", "content": query}]
        )
        response_content = response.choices[0].message.content
        return jsonify({"response": response_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Flask app running with fine-tuned model!")
    app.run(debug=True)