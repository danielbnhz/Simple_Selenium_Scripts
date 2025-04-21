from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() 

driver.get("https://libgen.rs/")


search_box = driver.find_element("name", "req")  
search_query = input("What do you wish to search for? Input simple string:\n")
search_box.send_keys(search_query)  
search_box.send_keys(Keys.RETURN) 

input("Press any button to continue")

# Step 4: Close the browser
driver.quit()
