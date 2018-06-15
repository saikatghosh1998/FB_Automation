
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path = "C:\Program Files\Selenium\chromedriver")
driver.get("https://www.facebook.com")
driver.maximize_window()
username='********'
password='********'
xpathbutton='//input[@value="Log In"]'

emailfield='email'
passfield='pass'

emailfieldelement=driver.find_element_by_id(emailfield)
passfieldelement=driver.find_element_by_id(passfield)
loginButton = driver.find_element_by_xpath(xpathbutton)

emailfieldelement.send_keys(username)
passfieldelement.send_keys(password)
loginButton.click()