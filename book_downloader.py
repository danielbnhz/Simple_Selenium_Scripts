from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def start_driver():
    driver = webdriver.Chrome() 
    driver.get("")
    return driver
def perform_search(driver):
    
    search_box = driver.find_element("name", "req")  
    search_query = input("What do you wish to search for? Input simple string:\n")
    search_box.send_keys(search_query)  
    search_box.send_keys(Keys.RETURN) 



def parse_results(driver):
    table = driver.find_elements(By.CLASS_NAME,"c")
    rows = driver.find_elements(By.TAG_NAME, 'tr')



def main():
    try:
        driver = start_driver()
        perform_search(driver)
        parse_results(driver)
        input("Press any button to continue:\n")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

