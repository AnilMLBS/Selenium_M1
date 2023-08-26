from selenium.webdriver import Chrome
from time import sleep
driver = Chrome(executable_path=r"../drivers/Chromedriver.exe")
#driver.get("https://www.fb.com")
driver.get("E:\Q-Spiders - Python\Sunil-Notes\Selenium Notes\htmlsamplecode.html")
driver.maximize_window()
driver.find_element("link text","Facebook").click()
sleep(3)
#driver.find_element("link text","Forgotten password?").click()
#sleep(5)
#driver.find_element("link text","Forgotten account?").click()
driver.find_element("partial link text","password?").click()
sleep(5)
driver.find_element("partial link text","account?").click()
