import send_telegram

message = send_telegram.TelegramMessage
img = "a.jpeg"
caption = "Cristiano Ronaldo!"

message.sendPhotoToTelegram(img=img, caption=caption)
