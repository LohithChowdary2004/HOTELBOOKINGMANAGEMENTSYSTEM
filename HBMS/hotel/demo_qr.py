#
#
# # import qrcode
# # first_name="Y.Lohith"
# # last_name="Chowdary"
# # email="lohithchowdary2004@gmail.com"
# # phone_number="9676190239"
# # vcar=f"BEGIN:VCARD\nVERSION:3.0\nN:{first_name};{last_name};;;\nFN:{first_name}\nEMAIL:{email};TYPE=INTERNET:{email}" \
# #      f"\nTEL;TYPE=CELL:{phone_number}\nEND:VCARDE"
# # img=qrcode.make(vcar)
# # img.save('contact.png')
#
import qrcode
import os
# Specify the directory where you want to save the image
output_directory = "static/hotel/images"

# Ensure the directory exists; create it if it doesn't
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

first_name = "Y.Lohith"
last_name = "Chowdary"
email = "lohithchowdary2004@gmail.com"
phone_number = "9676190239"
vcar = f"BEGIN:VCARD\nVERSION:3.0\nN:{first_name};{last_name};;;\nFN:{first_name}\nEMAIL:{email};TYPE=INTERNET:{email}" \
     f"\nTEL;TYPE=CELL:{phone_number}\nEND:VCARDE"

img = qrcode.make(vcar)

# Specify the full path, including the desired directory, to save the image
image_path = os.path.join(output_directory, "templates/hotel/contact.png")
img.save(image_path)

print(f"QR code saved to {image_path}")





#
# import qrcode
# from PIL import Image
#
# first_name = "Y.Lohith"
# last_name = "Chowdary"
# email = "lohithchowdary2004@gmail.com"
# phone_number = "9676190239"
# vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{first_name};{last_name};;;\nFN:{first_name}\nEMAIL:{email};TYPE=INTERNET:{email}" \
#      f"\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"
#
# # Create a QR code instance
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(vcard)
# qr.make(fit=True)
#
# # Create a QR code image
# img = qr.make_image(fill_color="black", back_color="white")
#
# # Save the image
# img.save("contact.png")
# img.show()  # This displays the QR code using your default image viewer

