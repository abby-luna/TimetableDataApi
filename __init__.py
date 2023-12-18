from auth import Authentication
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your ChromeDriver executable
chrome_driver_path = 'chromedriver.exe'

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

try:
    creds = Authentication()

    driver.get('https://timetable.lit.ie/SWS2022_Student/login.aspx')
    username_input = driver.find_element(By.ID, 'tUserName')
    password_input = driver.find_element(By.ID, 'tPassword')
    submit = driver.find_element(By.ID, "bLogin")

    username_input.send_keys(creds.getKNo())
    password_input.send_keys(creds.getPass())
    submit.click()

    student_set = driver.find_element(By.ID, "LinkBtn_StudentSet")
    student_set.click()

    dropdown = driver.find_element(By.ID, "dlObject")
    selects = dropdown.find_elements(By.XPATH, f"//select[@id='dlObject']//option")
    # //max(selects, lambda x: len(x.get_attribute("innerHTML")))
    
    print("subjectId,campus,courseName,yearOfStudy,group")
    for i in selects:
        print(i.get_attribute("innerHTML"))



except Exception as E:
    print(E)
    # Close the browser
    #driver.quit()
