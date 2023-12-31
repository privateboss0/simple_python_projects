import qrcode

# link which represents the QR code to the youtube link or any website you want
link = "https://www.youtube.com/watch?v=3ji4PcqIBEg"

# Generate and save QR code
image = qrcode.make

qrcode.make(link).save("Youtubelink.png")
