from tkinter import *   
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle



class App(Frame):   
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=1500, height=4500, **kwargs)
        self.pack(fill=BOTH)

        self.message = Label(self, text="Accidents Details.")
        self.message.pack()
        
        self.bouton_quitter = Button(self, text="Quit", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red")
        self.bouton_cliquer.pack(side="right")
    
fen = Tk()
fen.mainloop
f = App(fen)
