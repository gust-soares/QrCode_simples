import qrcode

image = qrcode.make("https://youtube.com")
image.save("first_qrcode.jpg")
