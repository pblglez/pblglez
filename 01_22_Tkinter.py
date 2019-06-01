from tkinter import *
from tkinter import ttk

numVentanas = 0
pos_y = 0
pos_x = 0
a = "borrar esto es una prueba"

def abrirM():
    abrir(True)

def abrir(modal=False):
    global pos_y, pos_x, mainWindow
    dialogo = Toplevel()
    pos_y += 50
    pos_x += 50
    
    dialogo.geometry("200x100+{}+{}".format(pos_x, pos_y))
    dialogo.resizable(0, 0)
    id = dialogo.winfo_id()
    dialogo.title("Dialogo: {}".format(id))
    
    boton = ttk.Button(dialogo, text="Cerrar", command=dialogo.destroy)
    boton.pack(side=BOTTOM, padx=20, pady=20)
    
    if modal:
        dialogo.transient(master=mainWindow)
        dialogo.grab_set()
    
    mainWindow.wait_window(dialogo)
    

mainWindow = Tk()
mainWindow.resizable(0, 0)
mainWindow.geometry("300x200+500+50")
mainWindow.title("Main Window")

openBtn = ttk.Button(mainWindow, text="Open", command=abrir)
openBtn.pack(side=BOTTOM, padx=20, pady=20)

openBtnM = ttk.Button(mainWindow, text="Modal", command=abrirM)
openBtnM.pack(side=BOTTOM, padx=20, pady=20)

mainWindow.mainloop()