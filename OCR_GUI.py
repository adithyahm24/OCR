import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as tkk

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def convert(img):
    img = Image.open(img)
    text = pytesseract.image_to_string(img)
    return text


class OCR(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text = ''
        self.img = None
        self._frame = tk.Frame(self)
        self._frame.pack()
        self.config(background="#01F3B3")
        self._frame.config(background = "#01F3B3")

        t = tkk.Label(self._frame, text="Optical Charactor Recognition",background = '#F3D601')
        t.config(font = ("Arial",40,'bold'))

        t.grid(row=0, column=0)
        tk.Label(self._frame,text = '',bg = '#01F3B3').grid(row = 1,column =0)
        b1 = tk.Button(self._frame,
                       text=" Select a File ",
                       height = 5,
                       width = 60,
                       command=self.con,
                       bg = '#FE831D')
        b1.grid(row=3, column=0)

    def con(self):
        self.img = filedialog.askopenfilename(initialdir='/', title='Select a Image', filetype=(
            ('JPG', '*.jpg'), ('PNG', '*.png'), ('ALL_FILES', '*.*')))
        self.text = convert(self.img)
        t = tk.Text(self._frame,width = 100)
        t.insert(1.0,self.text,)
        t.grid(row=5, column=0)


OCR().mainloop()
