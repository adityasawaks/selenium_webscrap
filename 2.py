from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://www.google.com/")
input=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
input.send_keys("fsf")
search = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[1]/a")
search.click()


#driver.quit()