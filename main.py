# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = 'c:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.nli.org.il/')
time.sleep(3)
element = driver.find_element(By.TAG_NAME, "button")
element.click()

# (By.CSS_SELECTOR("button.understood font-weight-bold"))
# onclick="AddAcceptUseCookies()"
# (SELECTOR("input[type='button']")).click()
# driver.findElement(By.cssSelector("input[type='button']")).click();

#       *** IN PROGRESS ***
