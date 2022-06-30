from tkinter import messagebox
from app import Aplicacion

class Funcion:
    __app= Aplicacion

    def __init__(self):
        self.__app= Aplicacion()
    

    def calcular(self):
        a = float(self.__app.getaltura().get())
        b = float(self.__app.getpeso().get())
        if a != '' and b != '':
            try:
                valor = float(b / a)
                if valor < 18.5:
                    self.__app.getresultado.set(valor)
                    self.__app.gettippeso.set("Peso inferior al normal")
                elif 18.5 < valor < 24.9:
                    self.__app.getresultado.set(valor)
                    self.__app.gettippeso.set("NORMAL")
                elif 25 < valor < 29.9:
                    self.__app.getresultado.set(valor)
                    self.__app.gettippeso.set("PESO SUPERIOR AL NORMAL")
                elif valor > 30:
                    self.__app.getresultado.set(valor)
                    self.__app.gettippeso.set("OBESIDAD")
            except ValueError:
                messagebox.showerror(title="Error de tipo", message="Debe ingresar un valor numerico")
                self.__app.getaltura.set('')
                self.__app.getpeso.set('')
                self.__app.altura.focus()
        else:
            self.__app.getaltura.set('')
            self.__app.getpeso.set('')

    def limpiar(self):
        self.__app.getaltura.set("")
        self.__app.getpeso.set('')
        self.__app.gettippeso.set('')
        self.__app.getresultado.set("")
        self.__app.altura.focus()
