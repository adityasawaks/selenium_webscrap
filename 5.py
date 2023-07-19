from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(400)
driver.get("https://")

search = driver.find_element(By.XPATH,"/html/body/form/div[4]/div/div[1]/div/div[3]/div[2]/div/input[1]")
search.send_keys("New Delhi")

searchI = driver.find_element(By.XPATH,"/html/body/form/div[4]/div/div[1]/div/div[3]/div[3]/input[1]")
searchI.click()

# try:
#     phone=driver.find_element(By.XPATH,f"/html/body/form/div[4]/div/div[1]/div/div[4]/table/tbody[12]/tr[2]/td[1]/a")
#     y=phone.text
# except:
#     y=""

# # phone=driver.find_element(By.XPATH,f"/html/body/form/div[4]/div/div[1]/div/div[4]/table/tbody[12]/tr[2]/td[1]/a")
# # y=phone.text
# print(y)

for i in range(1,31):
    try:
        phone=driver.find_element(By.XPATH,f"/html/body/form/div[4]/div/div[1]/div/div[4]/table/tbody[{i}]/tr[2]/td[1]/a")
        y=phone.text
    except:
        y=""

    try:
        driver.find_element(By.LINK_TEXT,y).click()
    except:
        pass
    try:
        phonee=driver.find_element(By.XPATH,"/html/body/form/div[5]/table/tbody/tr[2]/td/div/div/table/tbody/tr[3]/td")
        yy=phonee.text
    except:
        yy=""
    try:
        searchIi = driver.find_element(By.XPATH,"/html/body/form/div[5]/table/tbody/tr[1]/td/div/a[1]")
        searchIi.click()
    except:
        pass
        
    print(y)
    print(yy)