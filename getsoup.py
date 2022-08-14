from bs4 import BeautifulSoup
import requests

link = 'https://catalogorelogiosmytimes.kyte.site/'

page = requests.get(link)

soup = BeautifulSoup(page.content, 'html.parser') 

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
print(res)