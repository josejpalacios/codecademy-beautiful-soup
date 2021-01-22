# .children: Get children of tag
# .parents: Nagivate up HTML tree

import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# Loop through children of first div tag and print them
for child in soup.div.children:
  # Print child
  print(child)
