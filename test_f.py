from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import pickle


list =  [ "November", "December", "January", "February", "March","April", "May", "June", "July", "August",  "September", "October" ]

year_f = int(input("С какого года начать сбор данных? Напиши год"))
year_l = int(input("До какого года брать даные? Напиши год"))

year = year_l - year_f

try:

        #options
    options = webdriver.ChromeOptions()

        #change useragent
    useragent = UserAgent()
    options.add_argument(f"user-agent={useragent.random}")

    #disable webdriver mode
    options.add_argument("--disable-blink-features=AutomationControlled")

    #parser background mode!!!
    options.headless = True


    driver = webdriver.Chrome(options = options)
    driver.get("https://www.forexfactory.com/calendar")


    elem = driver.find_element(By.CLASS_NAME, "fade").click()


    elem = driver.find_element(By.NAME, "flex[Calendar_mainCal][impacts][medium]").click()
    elem = driver.find_element(By.NAME, "flex[Calendar_mainCal][impacts][low]").click()
    elem = driver.find_element(By.NAME, "flex[Calendar_mainCal][impacts][holiday]").click()
    elem = driver.find_element(By.NAME, "flexFilters").click()

    time.sleep(3)

    for i in range(len(year)):
        for i in range(len(list)):

            driver.find_element(By.CLASS_NAME, "flexTitle").click()
            elem = driver.find_element(By.NAME, "flex[Calendar_mainCal][begindate]")
            elem.clear()
            elem.send_keys(list[i+1], " 7, 2022")

            time.sleep(3)

            elem = driver.find_element(By.NAME, "flex[Calendar_mainCal][enddate]")
            elem.clear()
            elem.send_keys(list[i], "7, 2022")
            elem.send_keys(Keys.ENTER)

            time.sleep(3)

            elem = driver.find_element(By.CLASS_NAME, "calendar__table ")

            sort_data = elem.text

except Exception:
    print("Что-то с парсером не так.")
finally:
    driver.close()
    driver.quit()
