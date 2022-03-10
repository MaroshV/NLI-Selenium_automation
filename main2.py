from selenium import webdriver

#PATH = 'c:/webdrivers/chromedriver.exe'
#driver = webdriver.Chrome('PATH')
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
driver.get('https://www.pravda.sk')
