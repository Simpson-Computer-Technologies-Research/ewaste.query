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
import scraper

# // Initialize the flask app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# // Main route
@app.route("/")
def main():
    response_str: str = """
        <div style="margin: 20px;">
            <h1>Tristan's Search Engine</h1>
            <p>Welcome to Tristan's e-waste search engine. Input what you want to search for below.</p>
            <form action="search">
                <input type="text" name="q" placeholder="Search here" required>
                <input type="submit" value="Search">
            </form>
        </div>
    """
    response_str += open("initial_query.html", "r").read()
    return response_str


# // Search route
@app.route("/search")
def query():
    # // Get the query from the request args
    query = request.args["q"]

    # // Declare header response string
    response_str = (
        """
        <div style="margin: 20px;">
            <h1>Tristan's Search Engine</h1>
            <p>Welcome to Tristan's e-waste search engine. Input what you want to search for below.</p>
            <form action="search">
                <input type="text" name="q" placeholder="Search here" required>
                <input type="submit" value="Search">
            </form>
        </div>
        """
    )

    # // Loop through the pages
    for i in range(0, 4):
        response_str += scraper.scrape_page(
            f"https://www.bing.com/search?q={query}&PC=U316&FORM=CHROMN?first={i * 8}",
            response_str
        )

    # // Return the response string
    return response_str


# // Run the flask app
if __name__ == "__main__":
    app.run()
