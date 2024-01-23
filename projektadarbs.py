#bibliotēku importēšana un webdriver inicializācija
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()#(service=service, options=options)

#Tīmekļa vietnes apmeklēšana
url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)

#pogas "All matches" piespiešana
all_matches= driver.find_element(By.XPATH, value='//label[@analytics-event="All matches"]')
all_matches.click()

#tabulas rindu iegūšana
matches= driver.find_elements(By.TAG_NAME, value= 'tr')

#datu iegūšana no katras rindas
date=[]
home_team=[]
score=[]
away_team=[]

for match in matches:
    date.append(match.find_element(By.XPATH, value='./td[1]').text)
    home_team.append(match.find_element(By.XPATH, value='./td[2]').text)
    score.append(match.find_element(By.XPATH, value='./td[3]').text)
    away_team.append(match.find_element(By.XPATH, value='./td[4]').text)

#webdriver aizvēešana
driver.quit()

#datu pārvietojumi uz CSV failu
df=pd.DataFrame({'date':date, 'home team':home_team, 'score':score,'away team':away_team})
df.to_csv('football_data.csv')
print(df)
