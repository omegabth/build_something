from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL of the back-end service
BACKEND_URL = "http://backend:5001/contacts"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        limit = request.form.get("limit", type=int)
        if limit is None or limit < 1 or limit > 50:
            # If invalid input, limit to 10
            limit = 10

        # Get contacts from the back-end service
        response = requests.get(BACKEND_URL, params={"limit": limit})
        contacts = response.json()

        return render_template("index.html", contacts=contacts, limit=limit)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
