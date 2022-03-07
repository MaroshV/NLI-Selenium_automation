from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'c:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.nli.org.il/')

try:
    accept_cookies = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    accept_cookies.click()
except TimeoutException:
    print('No accept cookies')




# (By.CSS_SELECTOR("button.understood font-weight-bold"))
# onclick="AddAcceptUseCookies()"
# (SELECTOR("input[type='button']")).click()
# driver.findElement(By.cssSelector("input[type='button']")).click();

#       *** IN PROGRESS ***


