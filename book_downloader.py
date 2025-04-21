from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 

driver.get("https://libgen.rs/")


search_box = driver.find_element("name", "req")  
search_query = input("What do you wish to search for? Input simple string:\n")
search_box.send_keys(search_query)  
search_box.send_keys(Keys.RETURN) 


table = driver.find_elements("xpath","/html/body/table[3]/tbody")
for row in table:
    print(row.text)


input("Press any button to continue")

driver.quit()
