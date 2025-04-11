from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

sentence_starters = [
    "On a Saturday night I...",
    "My greatest fear is...",
    "The world would be better if..."
]

sentence_endings = {
    "On a Saturday night I...": [
        "summon raccoons.",
        "binge documentaries on cheese.",
        "fight my inner demons... with pizza."
    ],
    "My greatest fear is...": [
        "a sentient spreadsheet.",
        "being haunted by my old tweets.",
        "a world without WiFi."
    ],
    "The world would be better if...": [
        "everyone had a nap schedule.",
        "dogs ran the government.",
        "meetings ended with cake."
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "starter" not in request.form:
            starter = random.choice(sentence_starters)
            return render_template("index.html", starter=starter, endings=sentence_endings[starter])
        else:
            starter = request.form["starter"]
            ending = request.form["ending"]
            full_sentence = f"{starter} {ending}"
            return render_template("index.html", full_sentence=full_sentence)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
