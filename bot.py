from rivescript import RiveScript
from tkinter import *
from tkinter import ttk
import time


class Chat:
    def __init__(self,ventana):
        #Inicializamos la inteligencia artificial de Rivescript
        self.bot = RiveScript()
        self.bot.load_file('ferreteria.rive')
        
        self.bot.sort_replies()

        #Inicializamos la ventana de tipo GUI
        self.ventana=ventana
        self.ventana.title("ChatBot")
        #Creamos un marco que contendra los diferentes elementos
        marco=LabelFrame(self.ventana)
        marco.grid(row=0,column=0,columnspan=2,pady=20)  # Reduje el columnspan a 2 para que el botón esté en la misma fila que la caja de entrada de texto
        #Creamos un label que tendra con el texto Respuestas

        #Colocamos un elemento Text para mostrar las respuestas
        self.entRespuesta=Text(marco)
        self.entRespuesta.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipady=30)  # Modifiqué el columnspan a 2 para que el texto abarque toda la fila
        self.entRespuesta.focus()
        #Colocamos un entry para recibir las Preguntas

        self.entPregunta=Entry(marco)
        self.entPregunta.grid(row=1,column=0,padx=10,pady=10,ipady=7,ipadx=120)  # Modifiqué el column a 0 para que esté en la primera columna
        self.entPregunta.bind('<Return>', self.preguntar)
        self.entPregunta.focus()
        #Colocamos un boton la funcion preguntar que recibira una pregunta y retornara una respuesta gestionada por la IA
        btnPreguntarCrear=Button(marco, text="Enviar", command=self.preguntar, bg="blue", fg="white" ,height=2, borderwidth=5)
        btnPreguntarCrear.grid(row=1, column=1, padx=10, pady=10, sticky=W+E)  # Modifiqué el column a 1 para que esté en la segunda columna y agregué el padx para dar un espacio entre la caja de entrada de texto y el botón

    def escribir_respuesta(self, respuesta):
        for letra in respuesta:
            self.entRespuesta.insert(END, letra)
            self.entRespuesta.see(END)  # Desplaza automáticamente el contenido hacia abajo
            self.ventana.update_idletasks()  # Actualiza la ventana
            time.sleep(0.03)

    #Funcion que leera el entry entPregunta que generara un respuesta via rivescript y se muestra en entRespuesta
    def preguntar(self, event=None):
        pregunta = self.entPregunta.get()
        self.entRespuesta.insert(END, "Usuario: " + pregunta + "\n\n")
        self.entPregunta.delete(0, END)
        respuesta = self.bot.reply("localuser", pregunta)
        self.escribir_respuesta("Bot: ")
        self.escribir_respuesta(respuesta + "\n")

if __name__=="__main__":
    ventana=Tk()
    Chat(ventana)
    ventana.mainloop()













