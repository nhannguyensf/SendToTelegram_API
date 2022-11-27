import telegram

# this will send to Nhan's telegram
my_token = "5811414502:AAGx1n_NTi8ev93uD9cZLXLiRZYsvGJRB5s"

# Tạo bot
bot = telegram.Bot(token=my_token)

# Gửi thử text message
# bot.sendMessage(chat_id = "", text="Gưi từ PyCharm")
bot.sendPhoto(chat_id="1871882149", photo=open("a.jpg", "rb"), caption="Siuuuuu!")
