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
        pass 
        
        
    def tagUser(self):
        pass
    

    
    def run(self):
        self.login()
        self.navigateToGiveaway()
        for i in range(self.comments):
            self.tagUser()
            time.sleep(self.intervals)
        
        