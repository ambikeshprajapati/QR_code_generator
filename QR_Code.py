import qrcode
import cv2
x=input("Press (E) to encode, Press (D) to decode \n")
if x=="E" or x=="e":
    a=input("Enter the link or text that you want to convert into QR \n")
    img=qrcode.make(a)
    print("Save image as (name) ")
    b=input()
    c=".jpg"
    b=b+c
    img.save(b)
elif x=="D" or x=="d":
    d=cv2.QRCodeDetector()
    i=input("Enter the file name \n")
    val,_,_=d.detectAndDecode(cv2.imread(i))
    print(val)
else:                                      
    print("Invalid input ")