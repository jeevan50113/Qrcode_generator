import tkinter as T
import pyqrcode


window = T.Tk()
window.title("code generator")

def generator():

    url = entered_url.get()
    qr = pyqrcode.create(url)
    qrcode = qr.svg("qrcodegenerator.svg",scale=5)


label = T.Label(window,text="URL")
label.grid(row = 0,column = 0)


entered_url = T.Entry(window)
entered_url.grid(row = 2,column = 0)


button = T.Button(window,text="Generate")
button.grid(row=3,column=1)




window.mainloop()