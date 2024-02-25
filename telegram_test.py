import telepot
import time

class Sebastian():
    def __init__(self):
        self.bot = telepot.Bot(token='5757197805:AAGGx88LXt1SZwH4Lycj8KLslzatsNisZc4')

    def open(self):
        bot_info = self.bot.getMe()
        print(bot_info)
    def message(self,friend,msg):
        self.bot.sendMessage(friend,msg)
    def send_pic(self,friend,pic):
        self.bot.sendPhoto(friend,photo=open(pic, 'rb'))


if __name__ == "__main__":
    bot = Sebastian()
    bot.open()
    friend = 5449371759 # id Alexander Valdez Telegram userinfobot
    msg    = "Ya es hora de dormir"
    bot.message(friend,msg)
    pic    = "C:/Users/soporte/Pictures/Saved Pictures/BBVA_images.jfif"
    bot.send_pic(friend,pic)