import sys
import os
from serpapi import GoogleSearch

API_KEY = os.getenv("SERPAPI_KEY")

if not API_KEY:
    print("❌ Error: SERPAPI_KEY environment variable not set!")
    print("Please run: export SERPAPI_KEY=your_api_key_here")
    sys.exit(1)

def search_google(query):
    params = {
        "q": query,
        "api_key": API_KEY,
        "hl": "hi"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    print("\n🔎 खोज परिणाम:\n")

    for i, result in enumerate(results.get("organic_results", []), start=1):
        print(f"{i}. {result['title']}")
        print(result["link"])
        print()

if __name__ == "__main__":
    query = " ".join(sys.argv[1:])
    if not query:
        print("❌ Error: Please provide a search query")
        print("Usage: python serpsearch.py \"your search query\"")
        sys.exit(1)
    search_google(query)