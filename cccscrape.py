#! python3
# test_scrape.py - Learning opportunity to scrape course descriptions from
# university websites

#import libraries
import  requests, pprint
from bs4 import BeautifulSoup
from selenium import webdriver
import string

#indicate which website
url = 'http://www.ccc.edu/Pages/course-catalog.aspx'

#open url
driver = webdriver.Firefox()
driver.get(url)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J','L','M','N','O','P','R','S','T','V','Z']

import csv
outputFile = open('output.csv','w', newline='')
outputWriter = csv.writer(outputFile)
#PROBLEMS - ERROR WHEN AN ELEMENT CANNOT BE FOUND.
for letter in alphabet:
    elm = driver.find_element_by_link_text(letter)
    elm.click()
    driver.implicitly_wait(45)
    print("Now on all courses in letter " + str(letter))
    page = requests.get(url)
    # parse html using beautifulsoup
    soup = BeautifulSoup(driver.page_source,'html.parser')
    classtitle = soup.findAll('div', {'class': 'course-title'})
    coursecode = soup.findAll('div', {'class': 'course'})
    description = soup.findAll('div', {'class': 'course-desc'})
    prereq = soup.findAll('div', {'class': 'prereq-text'})
    credits = soup.findAll('span', {'class': 'credits'})
    #PROBLEMS - NEEDS TO UPDATE BASED ON ELEMENT
    for course in range(len(classtitle)):
        outputWriter.writerow([(classtitle[course].getText())])
        outputWriter.writerow([(coursecode[course].getText())])
        outputWriter.writerow([(description[course].getText())])
        outputWriter.writerow([(prereq[course].getText())])
        outputWriter.writerow([(credits[course].getText())])

print("Completed")
