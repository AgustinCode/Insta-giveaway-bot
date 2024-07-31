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
    
    
    def __init__(self):
        pass
        
    def findRecentGiveaways(self):
        giveaways = []
        #Logic to find recent giveaways (complex, last thing to implement)
        return giveaways
    
    
    def scrapeFollowers(self, account):
        self.account = account
        account_link = f"https://www.instagram.com/{self.account}"
        users = [] #Fill this list with JavaScript DOM exploit
        return users
    
    
    