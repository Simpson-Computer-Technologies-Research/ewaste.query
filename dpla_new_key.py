import requests

"""
Go to https://temp-mail.org/en/ and create a new burner email address.
Copy the email address and paste it into the string below.
"""

# // Put the email address here
email: str = "your_email_address_here"


# // Create a new API key
r = requests.post(f"https://api.dp.la/v2/api_key/{email}", headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}, timeout=5)

# // Print response
print(r.text)