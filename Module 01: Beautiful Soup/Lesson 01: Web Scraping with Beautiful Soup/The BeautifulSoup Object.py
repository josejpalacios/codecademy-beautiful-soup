# BeautifulSoup is a Python library that makes it easy for us to
# traverse an HTML page and pull out the parts we’re interested in.

import requests
# Import BeautifulSoup package
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content

# Create BeautifulSoup object using html.parser
soup = BeautifulSoup(webpage, "html.parser")
# Print soup
print(soup)
