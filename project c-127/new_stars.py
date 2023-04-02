from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data=[]
new_stars_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)



    planet_df_1 = pd.read_csv("updated_star_data.csv")

    for index, row in planet_df_1.iterrows():


     print(f"Data Scraping at hyperlink {index+1} completed")

    print(new_stars_data)

# Remove '\n' character from the scraped data
scraped_data = []

for row in new_stars_data:
    replaced = []
    ## ADD CODE HERE ##


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ['star_name','distance','mass','radius','lum']

new_planet_df_1 = pd.DataFrame(stars_data,columns = headers)

# Convert to CSV
new_planet_df_1.to_csv('updated_star_data.csv', index=True, index_label="id")


