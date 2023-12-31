import qrcode

First_Name = "Leo"
Last_Name = "Ola"
Email = "aolaxxxx@gmail.com"
Phone_Number = "+2346072389851"

# Create vCard content in a readable format
vcard_content = f"""
BEGIN:VCARD
VERSION:4.0
N:{Last_Name};{First_Name};;;
FN:{First_Name} {Last_Name}
EMAIL;TYPE=INTERNET:{Email}
TEL;TYPE=CELL:{Phone_Number}
END:VCARD
"""
# Generate QR code from the vCard data and save it to an image file
image = qrcode.make(vcard_content)
image.save("virtual_contact.png")