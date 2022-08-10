import qrcode
data="whatever"
qr=qrcode.QRCode(version=1,box_size=10,vorder=5)
qr.add_data(data)

qr.make(fit=True)
img=qr.make_image(fill_color='red'.back_color='white')
img.save('myQRcODE.jpg')
