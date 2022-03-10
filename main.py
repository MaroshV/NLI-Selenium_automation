from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#PATH = 'c:/webdrivers/chromedriver.exe'
#driver = webdriver.Chrome('PATH')
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
driver.get('https://www.nli.org.il/')

try:
    accept_cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    accept_cookies.click()
except TimeoutException:
    print('No accept cookies')

driver.implicitly_wait(30)
user_button = driver.find_element(By.ID, 'userBtn')
user_button.click()
login = driver.find_element(By.XPATH, '//*[@id="ulUser"]/li[1]/a').click()

# user_button = driver.find_element(By.XPATH, '//*[@id="userBtn"]/div/svg').click()
# login = driver.find_element(By.XPATH, '//*[@id="ulUser"]/li[1]/a').click()

username = driver.find_element(By.ID, 'loginusername')
username.clear()
username.send_keys('QATest1')
username.send_keys(Keys.RETURN)

password = driver.find_element(By.ID, 'loginpassword')
password.clear()
password.send_keys('123456')
password.send_keys(Keys.RETURN)

login_button = driver.find_element(By.CLASS_NAME, 'btn _btn blue fnt dologin-btn').click()

#                              *** IN PROGRESS ***

