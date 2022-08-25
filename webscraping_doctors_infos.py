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

try_search_doctors_btn_click = True

def search_doctors_btn_click():
  search_btn = driver.find_element_by_xpath("//button[@class='w-100 btn-buscar btnPesquisar']")
  search_btn.click()
  
  
def get_doctors_on_page():
  doctors = driver.find_elements_by_xpath("//div[@class='card-body']")
  
  for doctor in doctors:
    #book_html = doctor.find_element_by_xpath("//h3//a")
    html_content = doctor.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    doctor_name = soup.find(name='h4').string
    print(doctor_name)

time.sleep(10)
search_doctors_btn_click()
time.sleep(10)
get_doctors_on_page()
time.sleep(2)
driver.quit()


""" while try_search_doctors_btn_click:
  try:
    search_doctors_btn_click()
    time.sleep(10)
    get_doctors_on_page()
    try_search_doctors_btn_click = False
  except:
    print('sem dados') """


    












