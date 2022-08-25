import time
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

URL_BASE = "http://books.toscrape.com/"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(URL_BASE)

try_search_doctors_btn_click = True

def search_doctors_btn_click():
  time.sleep(4)
  books = driver.find_elements_by_xpath("//article[@class='product_pod']")
  
  for book in books:
    book_html = book.find_element_by_xpath("//h3//a")
    html_content = book.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    book_parser = soup.find(name='h3').string
    print(book_parser)

  
    
search_doctors_btn_click()
time.sleep(3)
driver.quit()
  
""" while try_search_doctors_btn_click:
  try:
    search_doctors_btn_click()
    try_search_doctors_btn_click = False
  except:
    print('sem dados') """


    












