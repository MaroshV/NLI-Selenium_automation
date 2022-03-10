from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
driver.get('https://www.nli.org.il/')
driver.maximize_window()

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

driver.implicitly_wait(30)
username = driver.find_element(By.ID, 'loginusername')
username.clear()
username.send_keys('modonrtest@gmail.com')
username.send_keys(Keys.RETURN)

password = driver.find_element(By.ID, 'loginpassword')
password.clear()
password.send_keys('Test2022')
password.send_keys(Keys.RETURN)

login_button = driver.find_element(By.CLASS_NAME, 'btn _btn blue fnt dologin-btn').click()

search_button = driver.find_element(By.CLASS_NAME, 'expended_search_btn js-trigger_search_btn').click()
search_query = driver.find_element(By.ID, 'searchQuery')
search_guery.clear()
search_query.send_keys('Atlit')
search_query.send_keys(Keys.RETURN)

#                              *** IN PROGRESS ***

