# /////////////////////////////////////////////////////////////////////////
# //                                                                     //
# //                                                                     // 
# //    Author: Tristan Simpson                                          //
# //                                                                     //     
# //    About: Custom Search Engine for finding e-waste information      //
# //                                                                     //
# //                                                                     //
# /////////////////////////////////////////////////////////////////////////

# // Import the required modules
from flask import Flask, request
from cache import Cache
import scraper, threading

# // Initialize the flask app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# // Initialize the cache
cache = Cache()

# // Response header
response_header = ("""
    <div style="margin: 20px;">
        <h1>Tristan's Search Engine</h1>
        <p>Welcome to Tristan's e-waste search engine. Input what you want to search for below.</p>
        <form action="search">
            <input type="text" name="q" placeholder="Search here" required>
            <input type="submit" value="Search">
        </form>
    </div>
""")

# // Main route
@app.route("/")
def main():
    return response_header + open("initial_query.html", "r").read()


# // Search route
@app.route("/search")
def query():
    # // Get the query from the request args
    query = request.args["q"]

    # // Request a new query
    def get_new_query():
        response_str = response_header

        # // Loop over pages
        for i in range(0, 2):
            response_str += scraper.scrape_page(
                f"https://www.bing.com/search?q={query}&PC=U316&FORM=CHROMN?first={i * 8}",
                response_str
            )
            
        # // Insert response string into cache
        cache.insert(query, response_str)

        # // Return the response string
        return response_str

    # // Check cache for query
    if cache.exists(query):
        threading.Thread(target=get_new_query).start()
        return cache.get(query)

    # // Return the response string
    return get_new_query()


# // Run the flask app
if __name__ == "__main__":
    app.run()
