#bibliotēku importēšana un Selenium Webdriver inicializēšana
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

#tīmekļa vietnes apmeklēšana
url="https://www.adamchoi.co.uk/corners/detailed"
driver.get(url)

#pogas ''All matches'' piespiešana
all_matches_button= driver.find_element(By.XPATH, value='//label[@analytics-event="All matches"]')
all_matches_button.click()

#Tabulas rindu iegūšana
tables= driver.find_elements(By.TAG_NAME, value='tr')

#datu iegūšana no katras rindas
date=[]
home_team=[]
score=[]
away_team=[]

for table in tables:
    date.append(table.find_element(By.XPATH, value='/td[1]').text)
    home_team.append(table.find_element(By.XPATH, value='/td[2]').text)
    score.append(table.find_element(By.XPATH, value='/td[3]').text)
    away_team.append(table.find_element(By.XPATH, value='/td[4]').text)

#WebDriver aizvēršana
driver.quit()

#Datu organizēšana
dataframe=pd.DataFrame({'date':date, 'home team':home_team,'score':score, 'away team':away_team})

#Datu pārvietošana uz csv failu
dataframe.to_csv('football_data.csv')


