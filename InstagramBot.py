from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from Crawler import Crawler
import time

class Bot:
    
    def __init__ (self, comments, users, links, intervals = 5):
        self.comments = comments #Times the bot tags someone
        self.users = users #List of users
        self.links = links #List of giveaway links
        self.intervals = intervals #Intervals between comments
        
        
    def login(self, user, passw):
        self.user = user
        self.passw = passw
        
        
    def navigateToGiveaway(self, links):
        for link in self.links:
            #Go to the link
            break
            
        pass
        
        
    def tagUser(self):
        for user in self.users:
            #Tag user
            break
        
        pass
    

    
    def run(self):
        self.login()
        self.navigateToGiveaway()
        for i in range(self.comments):
            self.tagUser()
            time.sleep(self.intervals)
        
        