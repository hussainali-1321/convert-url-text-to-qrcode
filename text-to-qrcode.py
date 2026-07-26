import qrcode
data= input("enter the url or number : ")
img = qrcode.make(data)
img.save("qr.pnj") 
img.show()
print(img)
print("QR code is ready and show ")