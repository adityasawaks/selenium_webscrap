from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://www.")


for i in range(2,26):
    try:
        phone=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[1]")
        y=phone.text
    except:
        y=""
    try:
        price=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]").text
    except:
        price=""
    try:
        mrp=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]").text
    except:
        mrp=""
    print("------------------------------------------------------")
    print(y)
    print(price)
    print(mrp)
    print("------------------------------------------------------")
nextpage = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]/span")
nextpage.click()
for i in range(1,9):
    for i in range(2,26):
        try:
            phone=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[1]")
            y=phone.text
        except:
            y=""
        try:
            price=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]").text
        except:
            price=""
        try:
            mrp=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]").text
        except:
            mrp=""
        print("------------------------------------------------------")
        print(y)
        print(price)
        print(mrp)
        print("------------------------------------------------------")
    nextpage = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[12]/span")
    nextpage.click()
for i in range(2,26):
    try:
        phone=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[1]/div[1]")
        y=phone.text
    except:
        y=""
    try:
        price=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]").text
    except:
        price=""
    try:
        mrp=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]").text
    except:
        mrp=""
    print("------------------------------------------------------")
    print(y)
    print(price)
    print(mrp)
    print("------------------------------------------------------")


# driver.quit()