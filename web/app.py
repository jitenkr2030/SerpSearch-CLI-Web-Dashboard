from flask import Flask, render_template, request
from serpapi import GoogleSearch

app = Flask(__name__)

API_KEY = "YOUR_SERPAPI_KEY"

def search_google(query):
    params = {
        "q": query,
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return results.get("organic_results", [])

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        query = request.form["query"]
        results = search_google(query)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)