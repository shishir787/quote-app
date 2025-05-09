from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Great things never come from comfort zones."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
