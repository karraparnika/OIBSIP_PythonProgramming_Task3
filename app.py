from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        length = int(request.form["length"])

        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        symbols = "!@#$%^&*"

        all_chars = uppercase + lowercase + digits + symbols

        password = ''.join(
            random.choice(all_chars)
            for _ in range(length)
        )

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
