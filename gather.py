from json import dumps, loads
from os import getenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
from time import sleep
load_dotenv()
login = getenv("login")
password = getenv("password")
login_url = "https://tsiauca.edupage.org/login/"
dashboard_url = "https://tsiauca.edupage.org/dashboard/eb.php?eqa=bW9kZT10aW1ldGFibGU%3D"
driver = webdriver.Chrome()
def until_find(by: By, staff: str, that=None, delay=.5):
    if that:
        action = lambda:[el for el in driver.find_elements(by, staff) if that(el)]
    else:
        action = lambda:driver.find_element(by, staff)
    while True:
        sleep(delay)
        try:
            el = action()
            if el:
                break
        except NoSuchElementException:
            pass
    return el
def until_lose(by: By, staff: str, that=None, delay=.5):
    while True:
        try:
            driver.find_element(by, staff)
            sleep(delay)
        except NoSuchElementException:
            break

with open("lessons.json", "r", encoding="utf-8") as f:
    old_data = loads(f.read())

driver.get(login_url)
driver.find_element(By.ID, "login_Login_1e1").send_keys(login)
driver.find_element(By.ID, "login_Login_1e2").send_keys(password)
driver.find_element(By.CLASS_NAME, "skgdFormSubmit").click()
until_lose(By.ID, "login_Login_1e1")
driver.get(dashboard_url)
until_find(By.TAG_NAME, "span", lambda el:el.get_attribute("title")=="Классы")
def find_lessons():
    lessons = []
    cabs = driver.find_elements(By.CLASS_NAME, "tt-cell")
    for cab in cabs:
        cab.click()
        lessons.append([div.text for div in driver.find_elements(By.TAG_NAME, "div") if div.get_attribute("style") == "font-size: 16px; margin-bottom: 5px;"])
    return lessons
info = []
[span.click() for span in driver.find_elements(By.TAG_NAME, "span") if span.get_attribute("title") == "Классы"]
facs = len(driver.find_element(By.CLASS_NAME, "dropDownPanel").find_elements(By.TAG_NAME, "a")[:-2])
try:
    for fac in range(14, facs):
        [span.click() for span in driver.find_elements(By.TAG_NAME, "span") if span.get_attribute("title") == "Классы"]
        fac = driver.find_element(By.CLASS_NAME, "dropDownPanel").find_elements(By.TAG_NAME, "a")[fac]
        fac.click()
        sleep(1)
        info.extend(find_lessons())
except:
    pass
print(info)
with open("lessons.json", "w", encoding="utf-8") as f:
    f.write(dumps(info+old_data))
# while 1:
    # sleep(5)
# x^3-6x^2+11x-5