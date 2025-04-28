from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def start_driver():
    driver = webdriver.Chrome() 
    driver.get("https://na.finalfantasyxiv.com/lodestone/playguide/db/")
    return driver
def perform_search(driver):
    
    # search_box = driver.find_element(By.NAME, "search")  
    search_boxes = driver.find_elements(By.NAME, 'q')
    search_box = search_boxes[1]

    search_query = input("What do you wish to search for? Input simple string:\n")
    search_box.send_keys(search_query)  
    time.sleep(2)
    search_box.send_keys(Keys.RETURN) 



def parse_results(driver):
    table = driver.find_elements(By.CLASS_NAME,"db-table")
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        print(row.text)



def main():
    try:
        i = 1
        driver = start_driver()
        perform_search(driver)
        parse_results(driver)
        turn_page = input("Next page? y/n: \n")
        while (turn_page=='y' or turn_page=='Y'):
            driver.find_elements(By.CLASS_NAME,'active').click()
            parse_results(driver)
            i += 1
            turn_page = input("Next page? y/n \n")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

