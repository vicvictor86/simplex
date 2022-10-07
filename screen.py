from msilib import RadioButtonGroup
from re import A
from tkinter import *

from matplotlib.pyplot import margins

class Application:
    def __init__(self, master=None):

        activeContainers = []

        valuesFunctionObjective = []
        valuesConstraint = []
        vectorB = []
        
        objProblem = IntVar()
        numberVariables = IntVar()
        numberConstraints = IntVar()

        numberVariables.set(1)
        numberConstraints.set(2)

        def clearActiveElements():
            for container in activeContainers:
                for element in container.winfo_children():
                    element.destroy()

        def objectiveProblem():
            return objProblem

        def numberOfVariables():
            return numberVariables

        def numberOfConstraints():
            return numberConstraints

        def functionCoefficients():
            return valuesFunctionObjective

        def modelProblem():
            clearActiveElements()

            print(objectiveProblem().get())
            print(numberOfVariables().get())
            print(numberOfConstraints().get())
            
            exp = "¹²³⁴⁵⁶⁷⁸⁹"

            self.firstCanva = Canvas(self.secondContainer, width=400, height=20)
            self.firstCanva.pack(side=LEFT)
            
            for i in range(0, numberOfVariables().get() + 2):

                if i == 0:
                    self.variableNumberLabel = Label(self.firstCanva, text="Variáveis", height=2, width=20)
                    self.variableNumberLabel["font"] = ("Arial", "12", "bold")
                    self.variableNumberLabel.grid(row=1, column=0)
                    
                    self.variableNumberLabel = Label(self.firstCanva, text="Função Objetivo", height=2, width=20)
                    self.variableNumberLabel["font"] = ("Arial", "12")
                    self.variableNumberLabel.grid(row=2, column=0)

                if i < numberOfVariables().get():
                    self.variableNumberLabel = Label(self.firstCanva, text="x"+exp[i], font=self.standardFont, height=2, width=6)
                    self.variableNumberLabel["font"] = ("Arial", "14", "bold")
                    self.variableNumberLabel.grid(row=1, column=i+1)
                    
                    self.variableNumber = Entry(self.firstCanva)
                    self.variableNumber["justify"] = "center"
                    aux = IntVar()
                    valuesFunctionObjective.append(aux)
                    self.variableNumber["width"] = 5
                    self.variableNumber["font"] = self.standardFont
                    self.variableNumber["textvariable"] = valuesFunctionObjective[i]
                    self.variableNumber.grid(row=2, column=i+1)
                elif i == numberOfVariables().get():
                    self.variableNumberLabel = Label(self.firstCanva, text="Relação", font=self.standardFont, height=2, width=6)
                    self.variableNumberLabel["font"] = ("Arial", "12", "bold")
                    self.variableNumberLabel["width"] = 10
                    self.variableNumberLabel.grid(row=1, column=i+1)
                elif i == numberOfVariables().get() + 1:
                    self.variableNumberLabel = Label(self.firstCanva, text="Lado Direito", font=self.standardFont, height=2, width=6)
                    self.variableNumberLabel["font"] = ("Arial", "12", "bold")
                    self.variableNumberLabel["width"] = 10
                    self.variableNumberLabel.grid(row=1, column=i+1)

            for i in range(0, numberOfConstraints().get()):
                self.variableNumberLabel = Label(self.firstCanva, text=f"Restrição {i+1}", height=2, width=20)
                self.variableNumberLabel["font"] = ("Arial", "12")
                self.variableNumberLabel.grid(row=3+i, column=0)

                valuesConstraint.append([])

                for j in range(0, numberOfVariables().get() + 2):
                    if(j < numberOfVariables().get()):
                        valuesConstraint[i].append(IntVar())
                        self.variableNumber = Entry(self.firstCanva)
                        aux = IntVar()
                        self.variableNumber["width"] = 5
                        self.variableNumber["font"] = self.standardFont
                        self.variableNumber["textvariable"] = valuesConstraint[i][j]
                        self.variableNumber["justify"] = "center"
                        
                        self.variableNumber.grid(row=3+i, column=j+1)
                    elif(j == numberOfVariables().get()):
                        mb =  Menubutton ( self.firstCanva, text="≤", relief=RAISED )
                        mb.grid(row=3+i, column=j+1)
                        mb.menu =  Menu ( mb, tearoff = 0 )
                        mb["menu"] =  mb.menu

                        # biggerEqual = IntVar()
                        # equal = IntVar()
                        # mb.menu.add_checkbutton ( label="≥", variable=biggerEqual )
                        # mb.menu.add_checkbutton ( label="=", variable=equal )
                    elif(j == numberOfVariables().get() + 1):
                        self.variableNumber = Entry(self.firstCanva)
                        aux = IntVar()
                        vectorB.append(aux)
                        self.variableNumber["width"] = 5
                        self.variableNumber["font"] = self.standardFont
                        self.variableNumber["textvariable"] = vectorB[i]
                        self.variableNumber["justify"] = "center"
                        self.variableNumber.grid(row=3+i, column=j+1)


            
            self.continueButton = Button(self.thirdContainer)
            self.continueButton["text"] = "Resolver Problema"
            self.continueButton["font"] = ("Calibri", "12")
            self.continueButton["height"] = 2
            self.continueButton["width"] = 16
            self.continueButton["command"] = solveProblem
            self.continueButton.pack()

        def solveProblem():
            clearActiveElements()
            for i in functionCoefficients():
                print(i.get())

        def initialScreen():
            self.max = Radiobutton(self.secondContainer, 
            text="Min",
            indicatoron = 0,
            width = 10,
            padx = 10, 
            variable=objProblem, 
            command=objectiveProblem,
            value=0).pack(anchor=W, side=LEFT)

            self.min = Radiobutton(self.secondContainer, 
                text="Max",
                indicatoron = 0,
                width = 10,
                padx = 10, 
                variable=objProblem, 
                command=objectiveProblem,
                value=1).pack(anchor=W, side=LEFT)

            self.variableNumberLabel = Label(self.thirdContainer, text="Numero de Variáveis", font=self.standardFont, height=2)
            self.variableNumberLabel.pack(side=TOP)

            self.variableNumber = Scale(self.thirdContainer)
            self.variableNumber["width"] = 20
            self.variableNumber["orient"] = HORIZONTAL
            self.variableNumber["from_"] = 1
            self.variableNumber["variable"] = numberVariables
            self.variableNumber["to"] = 10
            self.variableNumber.pack(side=TOP)

            self.constraintsNumberLabel = Label(self.fourthContainer, text="Numero de Restrições", font=self.standardFont, height=2)
            self.constraintsNumberLabel.pack(side=TOP)

            self.constraintsNumber = Scale(self.fourthContainer)
            self.constraintsNumber["width"] = 20
            self.constraintsNumber["orient"] = HORIZONTAL
            self.constraintsNumber["from_"] = 1
            self.constraintsNumber["variable"] = numberConstraints
            self.constraintsNumber["to"] = 20
            self.constraintsNumber.pack(side=TOP)

            self.continueButton = Button(self.fifthContainer)
            self.continueButton["text"] = "Continuar"
            self.continueButton["font"] = ("Calibri", "12")
            self.continueButton["width"] = 12
            self.continueButton["command"] = modelProblem
            self.continueButton.pack()

        self.standardFont = ("Arial", "11")

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 100
        self.secondContainer["pady"] = 20
        self.secondContainer.pack()
        activeContainers.append(self.secondContainer)

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 80
        self.thirdContainer["pady"] = 20
        self.thirdContainer.pack()
        activeContainers.append(self.thirdContainer)

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 40
        self.fourthContainer.pack()
        activeContainers.append(self.fourthContainer)

        self.fifthContainer = Frame(master)
        self.fifthContainer["pady"] = 40
        self.fifthContainer.pack()
        activeContainers.append(self.fifthContainer)

        self.title = Label(self.firstContainer, text="Método Simplex - Fase 2")
        self.title["font"] = ("Arial", "16", "bold")
        self.title.pack(side=BOTTOM)
        self.title.pack()

        self.problemObjective = Label(self.secondContainer, text="Objetivo do Problema", font=self.standardFont)
        self.problemObjective["width"] = 20
        self.problemObjective["height"] = 2
        self.problemObjective["font"] = self.standardFont
        self.problemObjective.pack(side=TOP)

        initialScreen()
            
        



root = Tk()
width= root.winfo_screenwidth()  
height= root.winfo_screenheight() 
root.geometry("%dx%d" % (width, height)) 
root.state(newstate="zoomed")
root.title('Método Simplex')
Application(root)
root.mainloop()