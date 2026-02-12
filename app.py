from flask import Flask, render_template, request, redirect
import string
import random
import os

app = Flask(__name__)

url_mapping = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        long_url = request.form.get("url")

        if long_url:
            code = generate_short_code()
            url_mapping[code] = long_url
            short_url = request.host_url + code

    return render_template("index.html", short_url=short_url)

@app.route("/<code>")
def redirect_url(code):
    long_url = url_mapping.get(code)

    if long_url:
        return redirect(long_url)
    return "URL not found", 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)