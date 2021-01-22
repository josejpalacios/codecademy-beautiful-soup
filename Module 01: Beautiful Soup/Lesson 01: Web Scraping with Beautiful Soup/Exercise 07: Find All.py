# .find_all(): Find all occurrences of a tag.

# Can use regex to get certain sets of tags
# Example: soup.find_all(re.compile("h[1-9]"))

# Can use a list tag names
# Example: soup.find_all(['h1', 'a', 'p'])

# Can use a dictionary of attributes using attrs
# Example soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

# Can use a function for additional logic
# Example: soup.find_all(function_name)

import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# Find all a tags
turtle_links = soup.find_all("a")
# Print turtle_links
print(turtle_links)
