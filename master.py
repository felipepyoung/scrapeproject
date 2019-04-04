#! python3
# test_scrape.py - Learning opportunity to scrape course descriptions from
# university websites

#import libraries
import  requests, pprint
from bs4 import BeautifulSoup
from selenium import webdriver

#indicate which website
url = 'http://www.jeffersonstate.edu/course-descriptions/'

#open url
driver = webdriver.Firefox()
driver.get(url)

links = []

#fetch linkElems
for a in driver.find_elements_by_css_selector("div.page-entry-content a"):
    linktext = (a.get_attribute('href'))
    links.append(linktext)

import csv
outputFile = open('output.csv','w', newline='')
outputWriter = csv.writer(outputFile)

for link in links:
    page = requests.get(link)
    # parse html using beautifulsoup
    soup = BeautifulSoup(page.content,'html.parser')
    #Find course names
    pElems = soup.select('p')
    for course in range(len(pElems)):
        outputWriter.writerow([(pElems[course].getText())])

outputFile.close()
