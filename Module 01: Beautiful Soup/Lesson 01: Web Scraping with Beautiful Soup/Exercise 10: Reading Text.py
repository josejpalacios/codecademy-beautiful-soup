# .get_text(): Retrieve text inside tag
# Will combine all text into one string.

# To separate texts from different tags,
# specify a separator character.
# Example: soup.get_text('|')

import requests
from bs4 import BeautifulSoup

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  # Add get_text()
  turtle_name = turtle.select(".name")[0].get_text()
  # Use get_text() with |; store as a list splitting by |
  turtle_data[turtle_name] = turtle.ul.get_text("|").split("|")
  
# Print turtle_data
print(turtle_data)
