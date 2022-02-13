from tkinter import *
from tkinter.filedialog import * #LIBRERIA PARA UTILIZAR FILEDIALOG
root=Tk() # para ventana

root.iconbitmap("pikachu.ico") #colocar icono
root.title("Proyecto Compiladores") #para poner el nombre de la ventana
root.config(background="#D1C0B9") #Color de fondo
root.rowconfigure(0,minsize=300,weight=1) #se configura el tamaño minimo de las filas
root.columnconfigure(0,minsize=600,weight=1) #se configura el tamaño minimo de las columnas

def abrirArchivo():

    ubicacion=askopenfilename(title="Abrir",initialdir="C:\\",filetypes=(("Archivos de texto",".txt"),("Todos los Archivos",".*")))
    archivo=open(ubicacion,"r")
    texto=""
    for linea in archivo:
        texto+=linea

    archivo.close()

    root.title(ubicacion)
    cuadroEscritura.insert(1.0,texto) #inserta el contenido del documento

barraMenu=Menu(root) #para indicar que pertenece a la ventana principal, pero contien lo demas
menuArchivo=Menu(barraMenu,tearoff=False) #es el submenu que esta dentro de la barra menu

barraMenu.add_cascade(label="Archivo",menu=menuArchivo) #se indica que el menu caera en cascada

menuArchivo.add_command(label="Abrir",command=abrirArchivo) # para las opciones que tendra el menu

framePrincipal=Frame(root,background="#E8D9CE",width=800,height=600)
framePrincipal.grid(row=0,column=0,sticky='nsew',padx=15,pady=15)


framePrincipal.config(width=800,height=600)
framePrincipal.rowconfigure(0,minsize=300,weight=1) #debe tener la misma configuracion que el root.rowconfigure
framePrincipal.columnconfigure(0,minsize=600,weight=1) #debe tener la misma configuracion que el root.columnconfigure

cuadroEscritura=Text(framePrincipal,wrap=WORD) #para crear el cuadro de texto
cuadroEscritura.grid(row=0,column=0,pady=10,ipadx=10,sticky='nsew')

barraScroll=Scrollbar(framePrincipal,command=cuadroEscritura.yview) #para la barra scroll
barraScroll.grid(row=0,column=1,sticky='nsew')
cuadroEscritura.config(yscrollcommand=barraScroll.set)


#MENU
root.config(menu=barraMenu)
root.mainloop()
