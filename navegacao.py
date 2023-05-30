import time
from selenium import webdriver

def navegar():
    driver = webdriver.Chrome()
    driver.get("####")
    time.sleep(1)

    # Clica e preenche o campos 
    driver.find_element("xpath", '//*[@id="pro_user_email"]').send_keys("######")
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="pro_user_password"]').send_keys("#######")
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="login_form"]/div[7]/div/button').click()
    time.sleep(1)
    driver.find_element("xpath", '/html/body/header/nav[2]/div/ul[1]/li[4]/a').click()
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="report_5"]/td[6]/a').click()
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="reporting"]/header/div/div[1]/div[2]/div[2]/a').click()
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="reporting"]/header/div/div[1]/div[2]/div[2]/ul/li[2]').click()
    time.sleep(3)
    
    driver.quit()