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
from flask import Flask
import scraper

# // Initialize the flask app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# // Main route
@app.route("/")
def main():
    return ("""
    <div style="margin: 50px;">
        <h2>Welcome to Tristan's E-Waste Search Engine!</h2>
        
        <p>To search, go to <strong>/query/{your query here}</strong></p>
        <p>Example: <a href="/query/ewaste">/query/ewaste</a></p>
    </div>
    """)

# // Search route
@app.route("/query/<query>")
def query(query: str):
    # // Declare header response string
    response_str = (
        """
        <h1 style="margin-top: 10px; margin-left: 10px;">
            Tristan's E-Waste Search Engine
        </h1>
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
