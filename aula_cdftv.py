import time
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

URL_BASE = "https://portal.cfm.org.br/busca-medicos/"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(URL_BASE)

try_now = True
def test():
  time.sleep(4)
  search_btn = driver.find_element_by_xpath("//button[@class='w-100 btn-buscar btnPesquisar']")
  search_btn.click()
  html_content = search_btn.get_attribute('outerHTML')
  print(html_content)

while try_now:
  try:
    test()
    try_now = False
  except:
    print('sem dados')
    












