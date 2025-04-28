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
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'searchInput'))
    )

    search_query = input("What do you wish to search for? Input simple string:\n")
    search_box.send_keys(search_query)  
    time.sleep(2)
    search_box.send_keys(Keys.RETURN) 



# def parse_results(driver):
#     table = driver.find_elements(By.CLASS_NAME,"c")
#     rows = driver.find_elements(By.TAG_NAME, 'tr')



def main():
    try:
        driver = start_driver()
        perform_search(driver)
        # parse_results(driver)
        input("Press any button to continue:\n")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

