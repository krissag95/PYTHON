#Import sys to include the Modules folder which contains the modules
import sys
sys.path.append('./Modules')
sys.path.append('./Images')
from Modules import ToDo
from tkinter import *

#------------------- Root frame -------------------------
raiz = Tk()
raiz.title("Agenda")
#raiz.resizable(False, False)
raiz.iconbitmap('./Images/icon.bmp')
raiz.config(bg = 'gray', padx = 15, pady = 10)

#------------------- Main frame -------------------------
MainFrame = Frame()
MainFrame.config(bg = 'lightyellow' , width='350', height='450')
MainFrame.pack(fill = 'both', expand = True)

raiz.mainloop()
