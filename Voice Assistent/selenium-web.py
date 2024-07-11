from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import  Service

service = Service(executable_path='C:\Windows\chromedriver.exe')
driver =webdriver.Chrome(service=service,options=Options)
driver.get('https://www.wikipedia.org')