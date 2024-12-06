# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:03:07 2024

@author: shinki
"""


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Ejemplo:DalasReview @Sjbdjdjd2")
users = input("Escribe tu arroba:")
users =users.split(sep=" ")


for user in users:
    if user[0] == "@":
        user = user[1:]

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    driver.get("https://x.com/" + user)
    time.sleep(2)








