import random
import undetected_chromedriver as uc
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

os.system("pip3 install selenium")
os.system("pip install webdriver-manager")
os.system("pip3 install undetected_chromedriver")

names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
"ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
"ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
"lydia", "charles", "pedro", "bradley"]
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

link = 'https://www.three.co.uk/Support/Free_SIM/Order'

s = Service(r"C:\Users\[User]\Desktop\drivre\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s,options=options)
driver.get(link) #opens link (three)

catchall = input("Enter catchall along with @ symbol: ")
postcode = input("Enter postcode with space: ")

fName = random.choice(names)
lName = random.choice(names)

nLength = 2
num = ''.join(random.choice(numbers) for i in range(nLength))
email = str(fName)+str(lName)+str(num)+catchall #chooses random two numbers and the randomly chosen first and last name, then attaches to catchall


select = Select(driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select')) #used for selecting value of exact address


driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[1]/span/input').send_keys(fName)
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[2]/span/input').send_keys(lName)
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[4]/span/input').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[5]/span/input').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[7]/span/input').send_keys(postcode)
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/button[1]').click()
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select')))
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/label[8]/span/select').click()
select.select_by_visible_text('[First line of address here, must match website]')
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1400662678121"]/button[2]')))
driver.find_element(By.XPATH, '//*[@id="1400662678121"]/button[2]').click()
#these find elements are quite self explanatory, finds fields and enters data