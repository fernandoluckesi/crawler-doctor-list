import time
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

URL_BASE = "https://portal.cfm.org.br/busca-medicos/"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(URL_BASE)

def save_doctor(doctor):
  

  with open("doctors_db.json") as file:
    doctors = json.load(file)["doctors"]
    doctors.append(doctor)

  with open("doctors_db.json", "w") as file:
    data = {
      "doctors": doctors
    } 
    json.dump(data, file)
    


def search_doctors_btn_click():
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  search_btn = driver.find_element(By.XPATH, "//button[@class='w-100 btn-buscar btnPesquisar']")
  search_btn.click()
  
  
def get_doctors_on_page():
  doctors = driver.find_elements(By.XPATH, "//div[@class='card-body']")

  if len(doctors) < 1:
    return doctors
  else:
    for doctor in doctors:
      html_content = doctor.get_attribute('outerHTML')
      soup = BeautifulSoup(html_content, 'html.parser')
      doctor_name = soup.find(name='h4').string
      get_doctor_crm = soup.find('div', attrs = {'class':'col-md-4'}).text
      doctor_crm = get_doctor_crm[6:].strip()
      doctor_specialist = ""
      get_doctor_specialists = soup.find_all('div', attrs = {'class':'col-md-12'})
      last_item_doctor_specialist = get_doctor_specialists[len(get_doctor_specialists) - 1].text
      if "Médico sem especialidade registrada" not in last_item_doctor_specialist:
        doctor_specialist = last_item_doctor_specialist
      else:
        doctor_specialist = "Médico sem especialidade registrada"
      doctor_data = {
        "name": doctor_name,
        "crm": doctor_crm,
        "specialty": doctor_specialist
      }
      save_doctor(doctor_data)
      print(doctor_data)
    return doctors


def next_page(page_number):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  next_page_btn = driver.find_element(By.XPATH, f"//li[@data-num='{str(page_number)}']")
  next_page_btn.click()
  

def scraper():
  page_number = 1
  try_search_doctors_btn_click = True
  time.sleep(3)
  while try_search_doctors_btn_click:
    try:
      search_doctors_btn_click()
      try_search_doctors_btn_click = False
    except:
      print("Click in 'Buscar' failed")

  while page_number <= 5:
    try_get_doctors_on_page = True
    try_next_page = True

    while try_get_doctors_on_page:
      time.sleep(3)
      doctors = get_doctors_on_page()
      if len(doctors) > 0:
        try_get_doctors_on_page = False
      else:
        print("Get doctors failed")

    page_number += 1
    
    while try_next_page:
      try:
        next_page(page_number)
        try_next_page = False
      except:
        print("Next page failed")
    
  driver.quit()
  
   
  
scraper()






    












