from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
stars_data=[]
scraped_data = []

def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body= bright_star_table.find('tbody')
    table_rows=table_body.find_all('tr')

    for row in table_rows:
        table_cols=row.find_all('td')
        print(table_cols)

        temp_list=[]

        for col_data in table_cols:
            headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
            print(col_data.text)

            data =col_data.text.strip()
            print(data)

            temp_list=[data]

            scraped_data(temp_list)  

    stars_data=[]
    for i in range(0,len(scraped_data)):
        stars_name= scraped_data[i][1]
        distance =scraped_data[i][3]
        mass =scraped_data[i][5]
        radius=scraped_data[i][6]
        lum=scraped_data[i][7]

        requried_data=[stars_name,distance,mass,radius,lum]
        stars_data.append(requried_data)
        print(stars_data)

headers =['star_name','distance','mass','radius','lum']
star_df_1=pd.DataFrame(stars_data,cloumns=headers)

star_df_1.to_csv('stars_data.cvs',index=True,index_label="id")

