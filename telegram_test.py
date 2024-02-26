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

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('chat_id:',chat_id)
    print('got command:',command)
    if command=='echo':
        bot.bot.sendMessage(chat_id,"Echo :D")

if __name__ == "__main__":
    bot = Sebastian()
    bot.open()
    friend = 5449371759 # GOOD - id Alexander Valdez Telegram userinfobot
    #friend = 5782251389 #-5782251389 # id Edson
    #friend = -4164870584 # GOOD - channel Group Test_bots Alexander Valdez
    #friend = -2125490739 # channel Group SOPHy
    #friend = 1583095431  # Boris Valdez
    msg    = "Buenos dias a todos, soy la IA Sebastian creada por la Magia"
    bot.message(friend,msg)
    pic    = "C:/Users/soporte/Pictures/Saved Pictures/BBVA_images.jfif"
    bot.send_pic(friend,pic)
    bot.bot.message_loop(handle)
    while(1):
        time.sleep(10)