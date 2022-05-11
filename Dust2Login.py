import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email = "quicajottiyu-7844@yopmail.com"
letras = string.ascii_letters + string.digits

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("https://dust2.gg/mi-cuenta/")
driver.find_element(By.ID,"username").send_keys(email)

for i in range(100):
    psw = ''.join(random.choice(letras) for i in range(20))
    driver.find_element(By.ID ,"password").send_keys(psw)
    driver.find_element(By.NAME,"login").send_keys(Keys.ENTER)