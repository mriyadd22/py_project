"""
To generate a QR-code, you have to use third-party libraries,
such as ( pip install qrcode and pip install "qrcode[pil]" ).

then, Import qrcode
"""

import qrcode

data = input("Enter the text or URL: ").strip()  #Remove any whitespace around the file name use 'strip()' method
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR Code saved as {filename}")
