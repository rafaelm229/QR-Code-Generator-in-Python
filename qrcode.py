import pyqrcode
from pyqrcode import QRCode

# Menu
print("*" * 25)
print("QR Code Generator\n")

# Receive the Data 
link = str(input("Enter Your Link:\n"))


# genearate the QR Code

url = pyqrcode.create(link)


# Create and Save the PNG file  naming "MyQR.svg"
url.svg("myQR.svg", scale=8)
print("\n" * 2 )
print("QR Code Created! \n")
print("*" * 25)


