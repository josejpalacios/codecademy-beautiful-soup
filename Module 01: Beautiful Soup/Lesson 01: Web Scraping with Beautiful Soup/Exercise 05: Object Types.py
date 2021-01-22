# Tags: Corresponds to an HTML Tag in the original document. Will get the first tag of element.
# .name: Get the name of the tag
# .attrs: A dictionary representing the attributes of the tag

# NavigableStrings: Pieces of text that is in the HTML tags on the page
# .string: Get the string inside the tag

import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# print first p tag
print(soup.p)
# print string of first p tag
print(soup.p.string)
