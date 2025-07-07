# import relevant libraries
import requests
from bs4 import BeautifulSoup

# define the url

url = "https://www.feedbooks.com/search?cat=FBFIC016000&query=feedbooks"

# send a request to get html code from that url

response = requests.get(url, headers={"Accept": "text/html"})

# parse the response

parsed_response = BeautifulSoup(response.text, "html.parser")

# format the parsed HTML response in a way that’s easier to read and print it out

print(parsed_response.prettify())