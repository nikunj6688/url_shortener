from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)


url_store = {}


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    code = ""

    for i in range(length):
        code += random.choice(characters)

    return code

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        long_url = request.form["long_url"]

        short_code = generate_short_code()

        url_store[short_code] = long_url

        short_url = f"http://127.0.0.1:5000/{short_code}"

        return render_template("index.html", short_url=short_url)

    return render_template("index.html")



@app.route("/<short_code>")
def redirect_url(short_code):
    if short_code in url_store:
        return redirect(url_store[short_code])
    else:
        return "URL not found"


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)