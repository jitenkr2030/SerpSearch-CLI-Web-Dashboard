import sys
from serpapi import GoogleSearch

API_KEY = "YOUR_SERPAPI_KEY"

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
    search_google(query)