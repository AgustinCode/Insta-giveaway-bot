from InstagramBot import Bot
from Crawler import Crawler

scrape_user_target = "aguss.193"


bot = Bot(comments=10,
          users=[],
          links=[],
          intervals=5
          )


crawler = Crawler(
    link=f"https://www.instagram.com/{scrape_user_target}/"
)