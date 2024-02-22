#https://chromedriver.chromium.org/downloads
#https://telepot.readthedocs.io/en/latest/
#https://selenium-python.readthedocs.io/locating-elements.html
#https://stackoverflow.com/questions/27948420/click-at-at-an-arbitrary-position-in-web-browser-with-selenium-2-python-binding
'''
MODIFICACIONES REALIZADAS DEBIDO A A VERSION DE selenium==4.18.1
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



import time

def slow_typing(element,text):
    for character in text:
        element.send:keys(character)
        time.sleep(0.3)

#def loggin():
#    click_menu = driver.find_element_by_css_selector("ul[@class='dropdown-menu']/li[1]").click()
#    click_menu.click()
    

driver  = webdriver.Chrome()
driver.get("http://sophy/experiment/1/")
driver.maximize_window()

time.sleep(1)


#dropdown = driver.find_element(By.CSS_SELECTOR,'a.dropdown-toggle')
dropdown = driver.find_element(By.XPATH,"//ul[@class='dropdown-menu']/li[2]")
dropdown.click()
time.sleep(1)
#dropdown.find_element(By.CSS_SELECTOR,'a.fa fa_play').click()

input("Escribe [q] y luego la  tecla [Enter] para finalizar: ")
