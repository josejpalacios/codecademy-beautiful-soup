# To get HTML, must make a request.
 
# Import requests library
import requests

# Make GET request
webpage_response = requests.get("https://content.codecademy.com/courses/beautifulsoup/shellter.html")
# Store content
webpage = webpage_response.content
# Print webpage
print(webpage)
