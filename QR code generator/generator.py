import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)

data = input("What message would you like to encrypt: \n")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
name = input("What name would you like to save your qr code as(add .png at the end): \n")
img.save(name)
