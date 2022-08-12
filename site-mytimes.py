from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import json 

link = 'https://catalogorelogiosmytimes.kyte.site/' 
driver = webdriver.Firefox() 
driver.get(link) 
 
# scrolling 
lastHeight = driver.execute_script("return document.body.scrollHeight")  
pause = 0.5
while True: 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")  
    if newHeight == lastHeight:
        break
    lastHeight = newHeight  
# ---

html = driver.page_source 

soup = BeautifulSoup(html, "html5lib")

results = soup.find(class_="infinite-scroll-component main_columns__3Oyp0 main_is-multiline__2UnxV")

cards_data = results.find_all("div", class_="main_column__y8FEH main_is-4__2KTdj") 
 
# source code of hotel cards 
res = []
for card in cards_data:  
    title = card.find('h4', attrs={'class': 'product_title__11Ti1'}) # ok 
    desc = card.find('div', attrs={'class': 'product_description__19mZJ product_crop-description__1wguP'}) # ok 
    images = [el["src"] for el in card.find_all('img') ] # ok 
    data = { 
        "title" : title.text, 
        "description" : desc.text, 
        "image" : images
    }   
    res.append(data)
  

with open('sample.json', 'w') as f:
    json.dump(res, f, ensure_ascii=False)

print("Created Json File")