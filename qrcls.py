import cv2
import qrcode
import inspect


class Qr:
    def __init__(self,data=None ,qr_byte=None ,file_path=None,):
        self.file_path = file_path
        self.data = data
        self.qr_byte = qr_byte
        if self.data:
            Qr.call_data(self)
            print('first func')
        elif self.qr_byte is not None:
            Qr.call_qr_byte(self)
            print('second fucn')
        elif file_path:
            ret=Qr.call_file_path(self)
            print(ret[0])
        else:
            print("Why are you even running the fucking code ?")


    def call_data(self):
        data = self.data
        qr=qrcode.QRCode()
        qr.add_data(data)

        qr.make(fit=True)
        img=qr.make_image(fill_color='red',back_color='white')
        img.save('myQRcODE.jpg')

    def call_qr_byte(self):

        # read the QRCODE image numpy ndarray
        image = self.qr_byte
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


    def call_file_path(self):
        # Name of the QR Code Image file
        filename = self.file_path
        # read the QRCODE image
        image = cv2.imread(filename)

        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        m=detector.detect(image)
        print('----------m--------------')
        print(m)
        # detect and decode
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        # if there is a QR code
        # print the data
        if vertices_array is not None:
          print('------------------------')
          print("QRCode data:")
        # #   print(len(data))
        # #   print(type(vertices_array))
        #   ts = vertices_array.tostring()
        #   tss = np.fromstring(ts, dtype = int)
        #   print((vertices_array))

          return (data, vertices_array)

        else:
          print("There was some error")
          return 0

gav = 'hey motherfucker'

# a = Qr(file_path='myQRcODE.jpg',)
# qr_byte=cv2.imread('myQRcODE.jpg'), data=None
a = Qr(file_path='qrcode_02.jpeg', qr_byte=None, data=None)
# arr = np.array([1, 2, 3, 4, 5, 6])
# ts = arr.tostring()
# print(np.fromstring(ts, dtype=int))
