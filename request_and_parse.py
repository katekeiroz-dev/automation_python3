# import relevant libraries
import requests
from bs4 import BeautifulSoup

# define the url

url = "https://www.thebookcentre.ie/"

# send a request to get html code from that url

response = requests.get(url, headers={"Accept": "text/html"})

# parse the response

parsed_response = BeautifulSoup(response.text, "html.parser")

#find all book titles
titles = parsed_response.find_all("h3", class_="product-title")

# Loop through the list of titles, using enumerate to get a number for each
for i, title in enumerate(titles, start=1):
    # Print the number and the text of the title
    print(f"{i}. {title.text}")
