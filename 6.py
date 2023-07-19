from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument('user-data-dir=C:\\Users\\adity\\Desktop\\ChromeProfile')
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.h.in")
t=[]
tt=[]
ttt=[]

for range_start in [6, 52, 102,141,188,235,282,329,376,423,470,517,564,611,658,705,752,799,846,893,940,987,1034,1081,1128,1175,1222,1269,1316,1363,1410,1457,1504,1551,1598,1645,1692,1739,1786,1833,1880,1927,1974,2021,2068,2115,2162,2209,2256,2303,2350,2397, 2444, 2491, 2538, 2585, 2632, 2679, 2726, 2773, 2820, 2867, 2914, 2961, 3008, 3055, 3102, 3149, 3196, 3243, 3290, 3337, 3384, 3431, 3478, 3525, 3572, 3619, 3666, 3713, 3760, 3807, 3854, 3901, 3948, 3995, 4042, 4089, 4136, 4183, 4230, 4277, 4324, 4371, 4418, 4465, 4512, 4559, 4606, 4653, 4700,4747, 4794, 4841, 4888, 4935, 4982, 5029, 5076, 5123, 5170,5217, 5264, 5311, 5358, 5405, 5452, 5499, 5546, 5593]:
    for i in range(range_start, range_start + 47):
        try:
            phone = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div/div[2]/div[3]/div[2]/div[{i}]/h3/a")
            y = phone.text
        except:
            y = ""
        time.sleep(3)
        print(i)
        print(y)
        t.append(i)
        tt.append(y)
        searchIo = driver.find_element(By.XPATH,f"/html/body/div[4]/div/div/div[2]/div[3]/div[2]/div[{i}]/h3/a")
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).click(searchIo).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[-1])
        try:
            phonee = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div")
            yy = phonee.text
        except:
            yy = ""
        print(yy)
        ttt.append(yy)
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        try:
            searchI = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div[3]/div[4]/a")
            searchI.click()
        except:
            pass



data_rec={'no':t,'name':tt,'details':ttt}
df=pd.DataFrame(data_rec)
df.to_csv('output.csv',index=False)