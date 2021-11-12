from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Users\\075146749\\Documents\\Belajar\\Project\\Javascript\\ChromeDriver\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)

print('=======================Tutorial 1 & 2=======================')

driver.get("https://techwithtim.net")
# For closing Tab
# driver.close()

search = driver.find_element_by_name('s')
search.clear()
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = driver.find_elements_by_tag_name("article")
    for article in articles:
      header = article.find_element_by_class_name("entry-summary")
      print(header.text) 
except: 
    print('error cuy')
finally:
    pass
# finally:
#     driver.quit()
print('=======================Tutorial 3=======================')

driver.get("https://techwithtim.net")
link2 = driver.find_element_by_link_text('Python Programming')
link2.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # buat next page sama back page
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
    print('Kelar')
except: 
    print('error cuy')
finally:
    pass


driver.quit()