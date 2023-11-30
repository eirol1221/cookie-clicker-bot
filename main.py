from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

SECS = 5
MINS = 1

s = Service(r"Your chromedriver path")
driver = webdriver.Chrome(service=s)

path = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(path)

date_now = datetime.now()
after_5secs = date_now + timedelta(seconds=SECS)
after_5mins = date_now + timedelta(minutes=MINS)

cookie = driver.find_element(By.ID, "cookie")

while date_now < after_5mins:
    cookie.click()

    cursor = driver.find_element(By.ID, "buyCursor")
    grandma = driver.find_element(By.ID, "buyGrandma")
    factory = driver.find_element(By.ID, "buyFactory")
    mine = driver.find_element(By.ID, "buyMine")
    shipment = driver.find_element(By.ID, "buyShipment")
    alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
    portal = driver.find_element(By.ID, "buyPortal")
    time_machine = driver.find_element(By.ID, "buyTime machine")

    if datetime.now() > after_5mins:
        cookies_per_sec = driver.find_element(By.ID, "cps")
        print(f"cookies/second: {float(cookies_per_sec.text.split(" : ")[0])}")
        break

    elif datetime.now() > after_5secs:
        if time_machine.get_attribute("class") != "grayed":
            time_machine.click()
        elif portal.get_attribute("class") != "grayed":
            portal.click()
        elif alchemy_lab.get_attribute("class") != "grayed":
            alchemy_lab.click()
        elif shipment.get_attribute("class") != "grayed":
            shipment.click()
        elif mine.get_attribute("class") != "grayed":
            mine.click()
        elif factory.get_attribute("class") != "grayed":
            factory.click()
        elif grandma.get_attribute("class") != "grayed":
            grandma.click()
        elif cursor.get_attribute("class") != "grayed":
            cursor.click()

        after_5secs = datetime.now() + timedelta(seconds=SECS)


