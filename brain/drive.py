from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging']) #Removes the DevTools listening msg


options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)