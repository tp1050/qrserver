import qrcode
import inspect

data=inspect.getsource(inspect.getmodule(inspect.currentframe()))

# data="whateverfdssssssssssssssssssssssssssssssssssssssfdsdfsdsfdsf"
qr=qrcode.QRCode()
qr.add_data(data)

qr.make(fit=True)
img=qr.make_image(fill_color='red',back_color='white')
img.save('myQRcODE.jpg')
