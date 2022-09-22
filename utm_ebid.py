from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
# chrome_options.add_argument("--headless")

url = 'https://bida.utm.my/User/Pembida/SemakNombor.aspx'

num_counter = 5000 #specify a start number
end_range = 5100 #specify end of range

julat_asal = num_counter

belum_jual_list = []

driver = webdriver.Chrome(service=Service("./chromedriver"))

while num_counter < end_range:
    driver.get(url)
    sleep(1)

    driver.find_element(By.XPATH, """/html/body/form/main/section/div/div/div/input""").click()
    driver.find_element(By.XPATH, """/html/body/form/main/section/div/div/div/input""").send_keys(num_counter)
    sleep(1)

    driver.find_element(By.XPATH, """/html/body/form/main/section/div/div/div/div[2]/a""").click()
    sleep(2)

    try:
        driver.find_element(By.XPATH, """/html/body/form/main/section/div/div[2]/div/div[5]/div/div/h3/span/span""") # find belum jual element text
    except NoSuchElementException:
        pass
    else:
        belum_jual_list.append(num_counter)

    num_counter += 1
    sleep(1)

if belum_jual_list == []:
    print("Semua nombor telah terjual pada julat " + str(julat_asal) + "-" + str(end_range))
else:
    print("\n ----- Nombor yang masih belum dijual pada julat " + str(julat_asal) + "-" + str(end_range) + " " + "-----\n")
    print(*belum_jual_list, sep = "\n")
   
driver.quit()
