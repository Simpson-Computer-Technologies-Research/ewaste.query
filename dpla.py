import requests, html

def query(query: str):
    # // Put your API key here
    api_key: str = "0f50a5575c58e285fc8646f1cf1aeecd"

    # // Make a request to the DPLA API
    r = requests.get(f"https://api.dp.la/v2/items?q={query}&api_key={api_key}", headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }, timeout=5)

    # // Declare an empty response string
    response_str: str = ""

    # // Loop through the api results
    for doc in r.json()["docs"]:
        data_provider_name: str = doc["dataProvider"]["name"]
        resource_url: str = doc["isShownAt"]

        # // Get the title from the api response
        resource_title: str = doc["sourceResource"]["title"][0]

        # // Get the description from the api response
        if "description" not in doc["sourceResource"]:
            continue

        # // Join the description list into a string
        resource_description: str = ("".join(
            f"{desc}<br>" for desc in doc["sourceResource"]["description"]
        ))[:300] + "...<br>"
        
        # // Add data to html response string
        response_str += html.wrap(
            f"{data_provider_name}: {resource_title}",
            resource_description,
            resource_url,
        )
    
    # // Return the response string
    return response_str
