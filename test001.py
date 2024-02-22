#https://chromedriver.chromium.org/downloads
#https://telepot.readthedocs.io/en/latest/
#https://selenium-python.readthedocs.io/locating-elements.html
#https://stackoverflow.com/questions/27948420/click-at-at-an-arbitrary-position-in-web-browser-with-selenium-2-python-binding

from selenium import webdriver
driver    = webdriver.Chrome(executable_path="/home/soporte/Downloads/chromedriver_linux64/chromedriver",options=driver_options)
driver.get("https://www.igp.gob.pe/informacion-institucional/seguridad_salud_trabajo/formatos/fscovid19/public/")
