import os
from flask import Flask, render_template, request
from serpapi import GoogleSearch

app = Flask(__name__)

API_KEY = os.getenv("SERPAPI_KEY")

def search_google(query):
    if not API_KEY:
        return []
    
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
    error_message = None

    if request.method == "POST":
        query = request.form["query"]
        if not API_KEY:
            error_message = "SERPAPI_KEY environment variable not set. Please configure it to use search functionality."
        else:
            results = search_google(query)

    return render_template("index.html", results=results, error_message=error_message)

if __name__ == "__main__":
    if not API_KEY:
        print("⚠️  Warning: SERPAPI_KEY environment variable not set!")
        print("Search functionality will not work without it.")
        print("Please run: export SERPAPI_KEY=your_api_key_here")
    app.run(debug=True)