import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Connected to" , url, "succesfully")
    print("The response code was: ", response.getcode())

# print("This is a site connectivity checker program")
# input_url = input("Input the url of the site you want to check: ")

# main(input_url)

#  input format  
#  https://www.google.com <- with no space 

# output 
# This is a site connectivity checker program
# Input the url of the site you want to check: https://www.google.com
# Checking connectivity 
# Connected to https://www.google.com succesfully
# The response code was:  200

#  shortene  code
import urllib.request as urllib

def main(url):
    response = urllib.urlopen(url)
    print("The response code was:", response.getcode())

input_url = input("Input the URL of the site you want to check: ")
main(input_url)


#  recommendation / bet practicecs 
# Best Practices:
# While the provided code snippet works, using the urllib module is considered a bit outdated. The recommended approach is to use the requests library for HTTP requests in Python, as it provides a more user-friendly and modern interface.
# Ensure error handling for cases where the URL is malformed or the connection fails.
# Consider adding exception handling to catch any potential errors that might occur during the connection process.

# and the  applies code to this best practices 

import urllib.request
# We use urllib.request specifically for web-related operations, such as making HTTP requests to fetch data from URLs
#  Real-World Application:
# Using urllib.request can be helpful when you need to perform tasks like:

# Retrieving data from web APIs or websites.
# Downloading files from the internet.
# Scraping web content for data extraction.
# Interacting with RESTful web services.
# Best Practices:
# If you're learning and starting with web-related tasks in Python, using urllib.request is a good way to familiarize yourself with the basics of HTTP requests.
# As your needs become more advanced or you encounter limitations in the standard library, you can explore more feature-rich libraries like requests.
def checksite(url):
    try:
        response = urllib.request.urlopen(url)
        print("Connecting to", url)
        print("Response code:", response.getcode())
    except urllib.error.URLError as e:
        print("Error:", e)

url = input("Enter the URL of the site you want to check: ")
checksite(url)
