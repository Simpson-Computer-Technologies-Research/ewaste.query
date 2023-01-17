import requests, html

def query(query: str):
    # // Put your API key here
    api_key: str = "f8e9e20b32c954ded7e5a527003a7bfd"

    # // Make a request to the Springer API
    r = requests.get(f"http://api.springernature.com/meta/v2/json?q={query}&api_key={api_key}", headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }, timeout=5)

    # // Declare an empty response string
    response_str: str = ""

    # // Loop through the api results
    for doc in r.json()["records"]:

        # // Get the data from the api response
        url: str = doc["url"][0]["value"]
        title: str = doc["title"]
        description: str = doc["abstract"][:300] + "..."

        # // Add data to html response string
        response_str += html.wrap(
            title,
            description,
            url
        )

    # // Return the response string
    return response_str

