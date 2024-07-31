from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class Crawler:
    
    
    def setupDriver(self):
    
        chromeOptions = Options()
        chromeOptions.add_argument("--disable-notifications")
        chromeOptions.add_argument("--disable-extensions")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=chromeOptions, service=service)
        self.wait = WebDriverWait(self.driver, 10)
    
    
    def __init__(self, link):
        self.link = link