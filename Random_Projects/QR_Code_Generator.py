import qrcode

# link which represents the QR code
link = "https://www.youtube.com/watch?v=3ji4PcqIBEg"

# Generate and save QR code
image = qrcode.make

qrcode.make(link).save("YTCode.png")