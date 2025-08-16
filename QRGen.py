# QR generator 
import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=JynFf1UTp1Q")
img.save("Kadhi_tu.png")


# QR generator with color, size

import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)

qr.add_data ("https://www.youtube.com/watch?v=JynFf1UTp1Q")
qr.make(fit = True)
img = qr.make_image(fill_color = "pink",back_color = "blue")
img.save("Kadhi_tu.png")


# Run 
# cd c:\python
# python QRGen.py