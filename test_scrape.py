#! python3
# test_scrape.py - Learning opportunity to scrape course descriptions from
# university websites

#import libraries
import  requests, pprint
from bs4 import BeautifulSoup

#indicate which website
url = 'http://www.jeffersonstate.edu/course-descriptions-bio/'

# query the website and return the html to variable 'page'
response = requests.get(url)

# parse html using beautifulsoup
soup = BeautifulSoup(response.content,'html.parser')

#Find course names
pElems = soup.select('p')

print(type(pElems))
print(len(pElems))
for course in range(len(pElems)):
    print(pElems[course].getText())
