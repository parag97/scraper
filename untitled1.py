import bs4
from selenium import webdriver
print("hello")
driver = webdriver.Firefox(executable_path="C:\\Users\\Naresh\\Anaconda3\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe")
driver.get("http://google.com")
print("hello",driver.title)

