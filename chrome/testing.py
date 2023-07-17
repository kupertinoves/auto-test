import time
import math
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
c='704777'
driver=webdriver.Chrome()
qwert='1212323232323'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    n=driver.find_element(By.CSS_SELECTOR,'#price')
    s=n.text
    while s !='$100' :
        n = driver.find_element(By.CSS_SELECTOR, '#price')
        s = n.text
        print(s)
        if s=='$100':
            driver.find_element(By.CSS_SELECTOR,'#book').click()
    n = driver.find_element(By.CSS_SELECTOR, '#input_value')
    s = n.text
    driver.find_element(By.CSS_SELECTOR,'#answer').send_keys(calc(int(s)))
    driver.find_element(By.CSS_SELECTOR,'#solve').click()





except Exception as ex:
    print(ex)
finally:
    time.sleep(10)
    driver.close()
    driver.quit()
