from msilib import RadioButtonGroup
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "11")

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 100
        self.secondContainer["pady"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 80
        self.thirdContainer["pady"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 40
        self.fourthContainer.pack()

        self.title = Label(self.firstContainer, text="Método Simplex - Duas Fases")
        self.title["font"] = ("Arial", "16", "bold")
        self.title.pack(side=BOTTOM)
        self.title.pack()

        self.problemObjective = Label(self.secondContainer, text="Objetivo do Problema", font=self.fontePadrao)
        self.problemObjective["width"] = 20
        self.problemObjective["height"] = 2
        self.problemObjective["font"] = self.fontePadrao
        self.problemObjective.pack(side=TOP)
        
        v = IntVar()

        def ShowChoice():
            print(v.get())
        
        self.max = Radiobutton(self.secondContainer, 
            text="Min",
            indicatoron = 0,
            width = 10,
            padx = 10, 
            variable=v, 
            command=ShowChoice,
            value=0).pack(anchor=W, side=LEFT)

        self.min = Radiobutton(self.secondContainer, 
            text="Max",
            indicatoron = 0,
            width = 10,
            padx = 10, 
            variable=v, 
            command=ShowChoice,
            value=1).pack(anchor=W, side=LEFT)
            

        self.constraintsNumberLabel = Label(self.thirdContainer, text="Numero de Restrições", font=self.fontePadrao, height=2)
        self.constraintsNumberLabel.pack(side=TOP)
        
        self.constraintsNumber = Entry(self.thirdContainer)
        self.constraintsNumber["width"] = 15
        self.constraintsNumber["font"] = self.fontePadrao
        self.constraintsNumber["validate"] = "key"
        self.constraintsNumber.pack(side=TOP)

        self.continueButton = Button(self.fourthContainer)
        self.continueButton["text"] = "Continuar"
        self.continueButton["font"] = ("Calibri", "10")
        self.continueButton["width"] = 12
        # self.continueButton["command"] = changeScreen()
        self.continueButton.pack()


root = Tk()
root.geometry("800x600")
root.title('Método Simplex')
Application(root)
root.mainloop()