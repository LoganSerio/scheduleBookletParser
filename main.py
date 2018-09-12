from pygrok import Grok
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests

#def scrapeSchedule():
url = 'https://appl101.lsu.edu/booklet2.nsf/mainframeset'
driver = webdriver.Chrome()
driver.get(url)

selectSem = Select(driver.find_element_by_name('%%Surrogate_SemesterDesc'))
selectSem.select_by_visible_text('Fall 2018')
selectDept = Select(driver.find_element_by_name('%%Surrogate_Department'))
selectDept.select_by_visible_text('COMPUTER SCIENCE ')
driver.find_element_by_xpath('/html/body/form/table[7]/tbody/tr[2]/td[3]/font/input').click()
respone = requests.get(url)
page = response.select_by_visible_text
soup = BeautifulSoup(page,'lxml')
print(soup.prettify())
    #with open('https://appl101.lsu.edu/booklet2.nsf/mainframeset') as site:
        