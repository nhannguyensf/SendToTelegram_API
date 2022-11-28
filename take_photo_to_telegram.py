import cv2
import telegram
from datetime import datetime

# this will send to Nhan's telegram
my_token = "5811414502:AAGx1n_NTi8ev93uD9cZLXLiRZYsvGJRB5s"
bot = telegram.Bot(token=my_token)
# define a video capture object
vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('Logitech webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        img_name = "Photo_{}.jpg".format(datetime.now().strftime("%H%M%S-%d-%m-%Y"))
        cv2.imwrite(img_name, frame)
        bot.sendPhoto(chat_id="1871882149", photo=open(img_name, "rb"), caption="Photo taken at {}.".format(datetime.now().strftime("%H:%M:%S-%d/%m/%Y")))
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
