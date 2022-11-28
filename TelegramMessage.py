import telegram

class TelegramMessage:
    my_token = "5811414502:AAGx1n_NTi8ev93uD9cZLXLiRZYsvGJRB5s"
    bot = telegram.Bot(token=my_token)

    def sendPhotoToTelegram(self, bot, img, caption):
        bot.sendPhoto(chat_id="1871882149", photo=open(img, "rb"), caption=caption)
