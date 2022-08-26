from asyncio import constants
from turtle import fillcolor
from more_itertools import consecutive_groups
import qrcode

input_url = "https://github.com/KamruzzamanAsif/"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size= 15, border=5, image_factory=None, mask_pattern=None)

qr.add_data(input_url)

qr.make(fit=True)

img = qr.make_image(fillcolor="red", back_color="white")
img.save("/home/asif/Python/Small Projects/QR.png")

print(qr.data_list)