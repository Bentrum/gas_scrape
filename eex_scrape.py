"""
Script for scraping of daily gas prices from the EEX website
"""

import time
import re
import datetime
from selenium import webdriver
import pymongo

url = "http://www.eex.com/de/marktdaten/erdgas/spotmarkt/daily-reference-price"
browser = webdriver.Firefox()
browser.get(url)
time.sleep(5)

number = browser.find_element_by_xpath(".//*[@id='content']/div/div/div/div/div/div/div/div/table/tbody[2]/tr[1]").text.split()
browser.quit()

price = {}
price["Market"] = number[0]
price["Execution"] = str(datetime.datetime.strptime(number[1], "%Y-%m-%d"))
price["Price"] = float(number[2].replace(",","."))


conn = pymongo.Connection("localhost")
db = conn.eex_databases_db
collection = db.daily_gas_price
collection.insert(price)
