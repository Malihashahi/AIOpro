import qrcode as qr


img = qr.make("WIFI:S:Bahar;T:WPA2;P:Allah@2001;;")

img.save('test1.png')