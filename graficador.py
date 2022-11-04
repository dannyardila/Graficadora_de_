import tkinter as t
from tkinter import messagebox
from matplotlib.pyplot import*
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2tk
import numpy as np
from math import*
win=t.Tk()
win.title("GRAFICADOR DE FUNCIONES")
win.geometry("900x900")
fig=Figure()
ax=fig.add_subplot(111)
print(style.available)


cvs=FigureCanvasTkAgg(fig,win)
cvs.draw()
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)
tlb=NavigationToolbar2tk(cvs,win)
tlb.update()
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)


entra_func=t.Entry(win,width=60)
entra_var=t.Entry(win,width=20)
entra_func.pack(side=t.RIGHT)
entra_func.pack(side=t.BOTTOM)










win.mainloop()