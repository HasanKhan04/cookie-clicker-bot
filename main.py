from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options=chrome_options)

service = Service(r"C:\Users\hasan\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
ids = [item.get_attribute("id") for item in store]
b = [item.find_element(By.CSS_SELECTOR, "b") for item in store]
b_text = [item.text.split("-")[-1].strip() for item in b if item != ""]
costs = []
for item in b_text:
    if item == "":
        b_text.remove(item)
    elif "," in item:
        item = item.replace(",", "")
        costs.append(int(item))
    else:
        costs.append(int(item))

timeout = time.time() + 5
end = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > end:
        cps = driver.find_element(By.ID, "cps")
        print(f"cookies/second: {cps.text}")
        break
    if time.time() > timeout:
        money = driver.find_element(By.CSS_SELECTOR, "#money")
        if "," in money.text:
            money = money.text.replace(",", "")
            money = int(money)
        else:
            money = int(money.text)
        max = 0
        item = ""
        for cost in costs:
            if max <= cost <= money:
                max = cost
        try:
            index = costs.index(max)
            buy = ids[index]
            to_click = driver.find_element(By.ID, buy)
            to_click.click()
            timeout = time.time() + 5
        except ValueError:
            pass



