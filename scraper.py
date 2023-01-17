import requests, bs4, html

# // Scrape data from the provided url
def scrape_page(url: str, curr_resp_str: str) -> str:

    # // Send a request to the url
    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }, timeout=5)

    # // Initialize bs4
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    # // Declare an empty response string
    response_str: str = ""

    # // Loop through the scrape results
    for i in soup.find_all('li', class_='b_algo'):
        # // Check if the result is none
        if i is None:
            continue

        # // Verify the result has a div and paragraph
        if i.p is None or i.div is None:
            continue

        # // Verify the result div has a header
        header = i.div.h2
        if header is None:
            continue
            
        # // Verify that the header has a url
        if header.a is None:
            continue

        # // No duplicate searches!
        if header.text not in curr_resp_str:
            response_str += html.wrap(
                header.text,
                i.p.text,
                header.a['href']
            )

    # // Return the response string
    return response_str