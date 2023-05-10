import sys
from selenium import webdriver
# import time
# import selenium.common.exceptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select

# Settings
DRIVER = 'firefox'


driver: webdriver = None
match DRIVER.lower():
    case 'firefox':
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    case 'chrome':
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service as ChromeService
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    case 'edge':
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from selenium.webdriver.edge.service import Service as EdgeService
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

if __name__ == '__main__':
    if not driver: sys.exit('Error while creating driver')
    websiteUrl = "https://github.com/AndreaGordanelli"
    driver.get(websiteUrl)
    input()
    driver.close()
