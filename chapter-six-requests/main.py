import requests
from io import BytesIO
from PIL import Image


r = requests.get("https://i.pinimg.com/originals/6a/f1/82/6af18235986718317a60f1202e940c21.jpg")

print("statuscode: ", r.status_code)
image = Image.open(BytesIO(r.content))

path = "./image.",image.format
print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("can not save image")
