import cv2
import qrcode
import inspect

 # show_data=0,show_qr=0
class Qr:
    def __init__(self,data=None ,qr_byte=None ,file_path=None,):
        self.file_path = file_path
        self.data = data
        self.qr_byte = qr_byte
        if self.data:
            call_data()
        elif self.qr_byte:
            call_qr_byte()
        elif file_path:
            call_file_path()

    def call_data(self):
        pass

    def call_qr_byte(self):
        pass
    def call_file_path(self):


        if self.file_path == None:
            return "No data was provided"

        # Name of the QR Code Image file
        filename = self.file_path
        # read the QRCODE image
        image = cv2.imread(filename)

        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        m=detector.detect(image)
        print(m)
        # detect and decode
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        # if there is a QR code
        # print the data
        if vertices_array is not None:
          print("QRCode data:")
          print(len(data))
          print(vertices_array)
          return (len(data),vertices_array)

        else:
          print("There was some error")
          return 0


        # self.show_data = show_data
        # self.show_qr = show_qr

    def decoder(self):
        if self.file_path == None and self.qr_byte==None:
            return "No data was provided"

        # Name of the QR Code Image file
        filename = self.file_path
        # read the QRCODE image
        image = cv2.imread(filename)

        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        m=detector.detect(image)
        print(m)
        # detect and decode
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        # if there is a QR code
        # print the data
        if vertices_array is not None:
          print("QRCode data:")
          print(len(data))
          print(vertices_array)
          return (len(data),vertices_array)

        else:
          print("There was some error")
          return 0

    def qrcode(self):
        if self.data == None:
            return "No data was provided "
        data = self.data
        # data="whateverfdssssssssssssssssssssssssssssssssssssssfdsdfsdsfdsf"
        qr=qrcode.QRCode()
        qr.add_data(data)

        qr.make(fit=True)
        img=qr.make_image(fill_color='red',back_color='white')
        img.save('myQRcODE.jpg')


# a = Qr(file_path='myQRcODE.jpg',)
a = Qr(file_path=None, qr_byte=cv2.imread('myQRcODE.jpg'), data=None)
if a.file_path:
    a.qrcode()
elif a.data:
    a.decoder()
elif a.qr_byte:
    a.decoder()

else:
    print("Why are you even running the fucking code ?")
