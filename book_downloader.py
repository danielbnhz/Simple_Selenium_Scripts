from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def start_driver():
    driver = webdriver.Chrome() 
    driver.get("https://libgen.rs/")
    return driver
def perform_search(driver):
    
    search_box = driver.find_element("name", "req")  
    search_query = input("What do you wish to search for? Input simple string:\n")
    search_box.send_keys(search_query)  
    search_box.send_keys(Keys.RETURN) 



def parse_results(driver):
    table = driver.find_elements(By.CLASS_NAME,"c")
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    i = 0
    j = 0
    for row in rows[:30]:
        cols = row.find_elements(By.TAG_NAME,'td')
        i = 0
        match j:
            case 0:
                j += 1
                pass
            case 1:
                j += 1
                pass
            case 2:
                j += 1
                pass

            case 3:
                j += 1
                pass
            case 4:
                j += 1
                pass
            case 5:
                for col in cols[0:]:
                    match i:
                        case 0:
                            print("ID:")
                            print(col.text)
                            
                        case 1:
                            print("Author(s):")
                            print(col.text)

                        case 2:
                            print("Title:")
                            print(col.text)

                        case 3:
                            print("Publisher:")
                            print(col.text)

                        case 4:
                            print("Year:")
                            print(col.text)

                        case 5:
                            print("Pages")

                            print(col.text)
                        case 6:
                            print("Language:")
                            print(col.text)

                        case 7:
                            print("Size:")
                            print(col.text)

                        case 8:
                            print("Extension:")
                            print(col.text)

                        case 11:
                            pass
                    i += 1
                    print("")
                # j+=1
                print("")
                print("")
                print("")
                print("")
            case 6:
                    break


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

