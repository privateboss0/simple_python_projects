import time
import pyotp
#import qrcode

secretkey = "3Private6Public7" 
#secretkey = pyotp.random_base32() Either use a static key or random key, both kept by the service provider.
#but the program works inversely with the recovery code app secretkey set to static, while MFA and Integration app secretkey in random.

counter = 0

dotp = pyotp.TOTP(secretkey)

while True:
  
  dotp_code = input("Enter the OTP from your Google/Microsoft Authenticator App: ")

  if dotp.verify(dotp_code):

    counter = 0

  
    print("Authentication successful!")

    # Make the API call.
    #Implement the API call here.