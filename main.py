from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

driver.implicitly_wait(5)

user_button = driver.find_element(By.TAG_NAME, 'svg').click()
login = driver.find_element(By.XPATH, '//*[@id="ulUser"]/li[1]/a').click()
#user_button = driver.find_element(By.XPATH, '//*[@id="userBtn"]/div/svg').click()
#login = driver.find_element(By.XPATH, '//*[@id="ulUser"]/li[1]/a').click()

username = driver.find_element(By.NAME, 'loginusername')
username.clear()
username.send_Keys('QATest1')
username.send_Keys(Keys.RETURN)

password = driver.find_element(By.NAME, 'loginpassword')
password.clear()
password.send_Keys('123456')
password.send_Keys(Keys.RETURN)

login_button = driver.find_element(By.CSS_SELECTOR, 'btn _btn blue fnt dologin-btn').click()


#                              *** IN PROGRESS ***








