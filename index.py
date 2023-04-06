import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image , ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkstyle = ttk.Style()
        ttkstyle.theme_use('default')
        ttkstyle.configure('white.TLabelframe',background = 'white',bd=0)
        ttkstyle.configure('white.TLabelframe.Label',background = 'white',foreground = 'red')
        F1 = tkFont.Font(family='Helvetica',size=16,weight='bold')

        drawingFrame = ttk.Labelframe(self,text='這裡是畫圖區',style='white.TLabelframe')
        drawingFrame.pack(padx=50,pady=50)

        linecanvas = tk.Canvas(drawingFrame,width=100,height=30,bd=0,highlightthickness=0,background='white')
        linecanvas.create_line((0,0),(100,0),width=20,fill='red')
        linecanvas.pack()

        ovalcanvas = tk.Canvas(drawingFrame,width=110,height=110,bd=0,highlightthickness=0,background='white')
        ovalcanvas.create_oval((10,10),(100,100),width=10,outline='red',fill='blue')
        ovalcanvas.pack()

        textcanvas = tk.Canvas(drawingFrame,width=110,height=50,bd=0,highlightthickness=0,background='white')
        textcanvas.create_text(0,0,text='ABC_中文',font=F1,anchor='nw')
        textcanvas.pack()

        mapcanvas = tk.Canvas(drawingFrame,width=300,height=300,bd=0,highlightthickness=0,background='white')
        taiwanimage = Image.open("map.png")
        newimage = taiwanimage.resize((300,300),Image.LANCZOS)
        self.taiwanimageTk = ImageTk.PhotoImage(newimage)
        mapcanvas.create_image(0,0,image = self.taiwanimageTk,anchor=tk.NW)
        mapcanvas.create_text(30,220,text='台灣',font=tkFont.Font(family='Helvetica',size=18),anchor='nw')
        mapcanvas.pack()

def main():
    windows = Window()
    windows.title("畫圖")
    windows.mainloop()

if __name__=='__main__':
    main()