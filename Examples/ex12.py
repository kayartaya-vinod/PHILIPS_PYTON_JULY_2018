'''
Testing a website using selenium and chromedriver
'''

from selenium import webdriver
from getpass import getpass

driver = webdriver.Chrome()
driver.get("https://vinod.co/login/")

mobile = input('Enter mobile: ')
password = getpass('Enter password: ')

tf_mobile = driver.find_element_by_name('mobile')
tf_mobile.send_keys(mobile)


tf_password = driver.find_element_by_name('passcode')
tf_password.send_keys(password)

btn_login = driver.find_element_by_id('btnLogin')
btn_login.click()


