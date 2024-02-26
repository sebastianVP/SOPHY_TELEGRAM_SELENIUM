#pip install python-telegram-bot
#pip install telegram
#taskkill /im python3.9.exe /f
from telegram import *
from telegram.ext import *
from requests import *

updater    = Updater(token='5757197805:AAGGx88LXt1SZwH4Lycj8KLslzatsNisZc4')
dispatcher = updater.dispatcher

randomPeopleText = "Random Person"
randomImageText  = "Random Image"

randomPeopleUrl = "https://thispersondoesnotexist.com/"
randomPImageUrl = "https://picsum.photos/1200"

likes    = 0
dislikes = 0

allowedUsernames = ["Alexandervp2022",None]
def startCommand(update:Update, context:CallbackContext):
    buttons = [[KeyboardButton(randomImageText)],[KeyboardButton(randomPeopleText)]]
    context.bot.send_message(chat_id=update.effective_chat.id,text="Welcome to my Little bot!",reply_markup=ReplyKeyboardMarkup(buttons))
    print(update.effective_chat.username)
    print(update.message.text)

def messageHandler(update: Update, context : CallbackContext):
    if update.effective_chat.username not in allowedUsernames:
        context.bot.send_message(chat_id=update.effective_chat.id,text="You are not allowed to use this bot")
        return
    if randomPeopleText in update.message.text:
        image = get(randomPeopleUrl).content
    if randomImageText in update.message.text:
        image = get(randomPImageUrl).content
    if image:
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id,media=[InputMediaPhoto(image,caption="")])
        buttons = [[InlineKeyboardButton("👍",callback_data="like")],[InlineKeyboardButton("👎",callback_data="dislike")]]
        context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons),text="Did you like the image?")

def queryHandler(update:Update, context:CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global likes,dislikes
    if "like" == query:
        likes +=1
    if "dislike" == query:
        dislikes +=1
    print(f"likes =>{likes} and dislikes =>{dislikes}")

dispatcher.add_handler(CommandHandler("start_point",startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))
updater.start_polling()
