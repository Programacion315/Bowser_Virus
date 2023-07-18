from random import randint
from tkinter import *
from tkinter import font
import tkinter as tk
import ctypes
from urllib import response
import requests

root = Tk()
root.overrideredirect(True) #Le quita el titulo, poner al final
root.wm_attributes('-transparentcolor', '#F0F0F0')
root.iconbitmap(default='C:\\Users\\T1\\Pictures\\icons\\mushroom.ico')

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

frame = tk.Frame(root, bd=2, relief='solid')
frame.pack()

font_file = 'fonts\\SuperMario256.ttf'


def openGitHub(event):
    import webbrowser
    webbrowser.open_new('https://github.com/Programacion315')


def getJoke():
    joke = requests.get(f"https://icanhazdadjoke.com/", headers= {"Accept":"application/json"})
    joke = joke.json() 
    print(joke['joke'])
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Bowser Joke")
    ventana_secundaria.configure(bg='#005ab4')

    halfWidth = root.winfo_screenwidth() // 2 - 1200 // 2
    halfHigh = root.winfo_screenheight() // 2 - 800 // 2

    loc = "1200x500+" + str(halfWidth) + "+" + str(halfHigh)
    ventana_secundaria.geometry(loc)
    
    Label(ventana_secundaria,text=joke['joke'],
             font=("Agency FB", 24), anchor="center", foreground= 'white', bg='#005ab4').place(relx=0.5, rely=0.5, anchor="center"),
    Label(ventana_secundaria,text='jluiso315',
             font=("Agency FB", 18), anchor="center", foreground= 'white', bg='#005ab4').place(relx=0.07, rely=0.9, anchor="center"),
    Label(ventana_secundaria,text='programacion315',
             font=("Agency FB", 18), anchor="center", foreground= 'white', bg='#005ab4').place(relx=0.9, rely=0.9, anchor="center"),


def position():
    restaAncho = int(ancho * 0.20)
    restaAlto = int(alto * 0.40)
    x, y = str(ancho - restaAncho), str(alto - restaAlto)
    loc = "300x265+" + x + '+' + y
    root.geometry(loc)
   
frameCnt = 60
frames = [PhotoImage(file='C:\\Users\\T1\\Documents\\Virtual_assistant_Browser-main\\Virtual_assistant_Browser-main\\proyecto\\bowser.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(15, update, ind)
label = Label(root)
label.pack()

getJoke()
position()
update(2)

root.mainloop()