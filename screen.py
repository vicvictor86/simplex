from msilib import RadioButtonGroup
from re import A
from tkinter import *
from matplotlib import container
from simplex import *

from matplotlib.pyplot import margins

class Application:
    def __init__(self, master=None):

        exp = "₁₂₃₄₅₆₇₈₉"

        tableau = {}

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
            strObjetiveProblem = ""
            if objProblem.get() == 1:
                strObjetiveProblem = "Maximizar"
            else:
                strObjetiveProblem = "Minimizar"

            self.objectiveProblem["text"]=f"Objetivo do Problema: {strObjetiveProblem}"
            return objProblem

        def numberOfVariables():
            return numberVariables

        def numberOfConstraints():
            return numberConstraints

        def functionCoefficients():
            return valuesFunctionObjective

        def modelProblem():
            clearActiveElements()

            for i in range(numberOfVariables().get()):
                tableau[f"x{i+1}"] = []
            tableau["b"] = []

            self.firstCanva = Canvas(self.secondContainer, width=400, height=20, borderwidth=0, highlightcolor="#003554", highlightbackground="#003554", background="#003554")
            self.firstCanva.pack(side=LEFT)
            
            for i in range(0, numberOfVariables().get() + 2):

                if i == 0:
                    self.variableNumberLabel = Label(self.firstCanva, text="Variáveis", height=2, width=20, background="#003554", foreground="#ffffff")
                    self.variableNumberLabel["font"] = ("Arial", "12", "bold")
                    self.variableNumberLabel.grid(row=1, column=0)
                    
                    self.variableNumberLabel = Label(self.firstCanva, text="Função Objetivo", height=2, width=20, background="#003554", foreground="#ffffff")
                    self.variableNumberLabel["font"] = ("Arial", "12")
                    self.variableNumberLabel.grid(row=2, column=0)

                if i < numberOfVariables().get():
                    self.variableNumberLabel = Label(self.firstCanva, text="x"+exp[i], font=self.standardFont, height=2, width=6, background="#003554", foreground="#ffffff")
                    self.variableNumberLabel["font"] = ("Helvetica", "18", "bold")
                    self.variableNumberLabel.grid(row=1, column=i+1)
                    
                    self.variableNumber = Entry(self.firstCanva)
                    self.variableNumber["justify"] = "center"
                    aux = IntVar()
                    valuesFunctionObjective.append(aux)
                    self.variableNumber["width"] = 5
                    self.variableNumber["font"] = self.standardFont
                    
                    self.variableNumber["bg"] = "#16425b"
                    self.variableNumber["fg"] = "#bbdefb"
                    self.variableNumber.configure(insertbackground="#bbdefb")
                    self.variableNumber["textvariable"] = valuesFunctionObjective[i]
                    self.variableNumber.grid(row=2, column=i+1)
                elif i == numberOfVariables().get():
                    self.variableNumberLabel = Label(self.firstCanva, text="Relação", font=self.standardFont, height=2, width=6, background="#003554", foreground="#ffffff")
                    self.variableNumberLabel["font"] = ("Arial", "12", "bold")
                    self.variableNumberLabel["width"] = 10
                    self.variableNumberLabel.grid(row=1, column=i+1)
                elif i == numberOfVariables().get() + 1:
                    self.variableNumberLabel = Label(self.firstCanva, text="Lado Direito", font=self.standardFont, height=2, width=6, background="#003554", foreground="#ffffff")
                    self.variableNumberLabel["font"] = ("Arial", "12", "bold")
                    self.variableNumberLabel["width"] = 10
                    self.variableNumberLabel.grid(row=1, column=i+1)

            for i in range(0, numberOfConstraints().get()):
                self.variableNumberLabel = Label(self.firstCanva, text=f"Restrição {i+1}", height=2, width=20, background="#003554", foreground="#ffffff")
                self.variableNumberLabel["font"] = ("Arial", "12")
                self.variableNumberLabel.grid(row=3+i, column=0)

                valuesConstraint.append([])

                for j in range(0, numberOfVariables().get() + 2):
                    if(j < numberOfVariables().get()):
                        valuesConstraint[i].append(IntVar())
                        self.variableNumber = Entry(self.firstCanva)
                        aux = IntVar()
                        self.variableNumber["width"] = 5
                        self.variableNumber["bg"] = "#16425b"
                        self.variableNumber["fg"] = "#bbdefb"
                        self.variableNumber.configure(insertbackground="#bbdefb")
                        self.variableNumber["font"] = self.standardFont
                        self.variableNumber["textvariable"] = valuesConstraint[i][j]
                        self.variableNumber["justify"] = "center"
                        
                        self.variableNumber.grid(row=3+i, column=j+1)
                    elif(j == numberOfVariables().get()):
                        mb =  Menubutton ( self.firstCanva, text="=", relief=RAISED )
                        mb["bg"] = "#16425b"
                        mb["fg"] = "#bbdefb"
                        mb.configure(activebackground="#bbdefb")
                        mb.grid(row=3+i, column=j+1)
                        mb.menu =  Menu ( mb, tearoff = 0 )
                        mb["menu"] =  mb.menu

                        # biggerEqual = IntVar()
                        # equal = IntVar()
                        # mb.menu.add_checkbutton ( label="≥", variable=biggerEqual )
                        # mb.menu.add_checkbutton ( label="≤", variable=equal )
                    elif(j > numberOfVariables().get()):
                        self.variableNumber = Entry(self.firstCanva)
                        aux = IntVar()
                        vectorB.append(aux)
                        self.variableNumber["width"] = 5
                        self.variableNumber["font"] = self.standardFont
                        
                        self.variableNumber["bg"] = "#16425b"
                        self.variableNumber["fg"] = "#bbdefb"
                        self.variableNumber.configure(insertbackground="#bbdefb")
                        self.variableNumber["textvariable"] = vectorB[i]
                        self.variableNumber["justify"] = "center"
                        self.variableNumber.grid(row=3+i, column=j+1)


            
            self.continueButton = Button(self.thirdContainer)
            self.continueButton["text"] = "Resolver Problema"
            self.continueButton["font"] = ("Calibri", "12")
            self.continueButton["bg"] = "#64b5f6"
            self.continueButton["activebackground"] = "#bbdefb"
            self.continueButton.configure(cursor="hand2")
            self.continueButton["height"] = 2
            self.continueButton["width"] = 16
            self.continueButton["command"] = solveProblem
            self.continueButton.pack()

        def solveProblem():
            clearActiveElements()
            for constraint in valuesConstraint:
                for coef in constraint:
                    tableau[f"x{constraint.index(coef)+1}"].append(coef.get())
            for coef in functionCoefficients():
                tableau[f"x{functionCoefficients().index(coef)+1}"].append(coef.get())
            for value in vectorB:
                tableau["b"].append(value.get())
            tableau["b"].append(0)

            # objective problem is max
            if objectiveProblem().get() == 1:
                for i in range(0, numberOfVariables().get()):
                    tableau[f"x{i+1}"][numberOfConstraints().get()] *= -1
                tableau[f"b"][numberOfConstraints().get()] *= -1

            tableauFinal, solution = simplex(tableau)

            self.firstCanva = Canvas(self.secondContainer, width=400, height=20, borderwidth=0, highlightcolor="#003554", highlightbackground="#003554", background="#003554")
            self.firstCanva.pack(side=LEFT)

            if solution == "optimal":
                self.e = Entry(self.firstCanva, width=10, justify="center",
                                    font=('Arial',16)) 
                self.e.insert(END, "Base")
                self.e.grid(row=0, column=0) 
                self.e["state"] = "readonly"

                optimalZ = tableauFinal[f"b"][numberOfConstraints().get()]	

                
                if objectiveProblem().get() == 1:
                    for value in tableauFinal:
                        if tableauFinal[value][-1] != 0:
                            tableauFinal[value][-1] *= -1

                for i in range(0, numberOfVariables().get() + 1):
                    if i < numberOfVariables().get():
                        if i < len(base):
                            self.e = Entry(self.firstCanva, width=10, justify="center",
                                            font=('Helvetica', 16, 'bold'))
                            if i < len(base):
                                self.e.insert(END, "x" + exp[int(base[i][1:])-1])
                            else:
                                self.e.insert(END, " ")
                            self.e.grid(row=i+1, column=0) 
                            self.e["state"] = "readonly"
                        elif i == len(base):
                            self.e = Entry(self.firstCanva, width=10, justify="center",
                                            font=('Helvetica', 16))
                            self.e.insert(END, " ")
                            self.e.grid(row=i+1, column=0) 
                            self.e["state"] = "readonly"

                        self.e = Entry(self.firstCanva, width=10,justify="center",
                                    font=('Helvetica',16, "bold")) 
                        self.e.insert(END, "x"+exp[i])
                        self.e.grid(row=0, column=i+1) 
                        self.e["state"] = "readonly"
                    elif i == numberOfVariables().get():
                        self.e = Entry(self.firstCanva, width=10,justify="center",
                                    font=('Helvetica',16)) 
                        self.e.insert(END, "b")
                        self.e.grid(row=0, column=i+1) 
                        self.e["state"] = "readonly"
                    for constraint in range(0, numberOfConstraints().get() + 1):
                        if list(tableauFinal.keys())[i] != "b":
                            self.e = Entry(self.firstCanva, width=10,justify="center",
                                        font=('Helvetica',16)) 
                            valueFloat = tableauFinal[f"x{i+1}"][constraint]
                            self.e.insert(END, f'{valueFloat:.1f}')
                            self.e.grid(row=constraint+1, column=i+1) 
                            self.e["state"] = "readonly"
                        else:
                            self.e = Entry(self.firstCanva, width=10,justify="center",
                                        font=('Helvetica',16)) 
                            
                            valueFloat = tableauFinal[f"b"][constraint]
                            
                            if constraint < numberOfConstraints().get():
                                self.e.insert(END, f"{valueFloat:.1f}")
                            else:
                                if tableauFinal[f"b"][constraint] > 0:
                                    self.e.insert(END, "Z+" + f"{valueFloat:.1f}")
                                    optimalZ *= -1
                                elif tableauFinal[f"b"][constraint] < 0:
                                    self.e.insert(END, "Z" + f"{valueFloat:.1f}")
                                else:
                                    self.e.insert(END, "Z")
                            self.e.grid(row=constraint+1, column=i+1) 
                            self.e["state"] = "readonly"

                self.secondCanva = Canvas(self.thirdContainer, width=400, height=20, borderwidth=0, highlightcolor="#001b2e", highlightbackground="#001b2e", background="#001b2e")
                self.secondCanva.pack(side=LEFT)

                self.e = Label(self.secondCanva, text="Solução Ótima",
                                    font=('Arial',14, "bold")) 
                self.e["bg"] = "#001b2e"
                self.e["fg"] = "#bbdefb"
                self.e.grid(row=0, column=1) 
                
                self.e = Label(self.secondCanva, width=10, justify="center",text=f"Z* = {optimalZ:.1f}",
                                font=('Helvetica',16)) 
                self.e["bg"] = "#001b2e"
                self.e["fg"] = "#bbdefb"
                self.e.grid(row=1, column=1) 

                self.e = Label(self.secondCanva, text="Variáveis básicas",
                                    font=('Arial',14)) 
                self.e["bg"] = "#001b2e"
                self.e["fg"] = "#bbdefb"
                self.e.grid(row=2, column=1) 
                for i in range(len(base)):
                    self.e = Label(self.secondCanva, width=10, justify="center", text=f"x{exp[int(base[i][1:])-1]}* = {tableauFinal['b'][i]:.1f}",
                                    font=('Helvetica',16)) 
                    self.e["bg"] = "#001b2e"
                    self.e["fg"] = "#bbdefb"
                    self.e.grid(row=3, column=i) 
                self.e = Label(self.secondCanva, text="Variáveis não-básicas",
                                    font=('Arial',14)) 
                self.e["bg"] = "#001b2e"
                self.e["fg"] = "#bbdefb"
                self.e.grid(row=4, column=1) 
                column = 0
                for i in range(0, numberOfVariables().get()):
                    if f"x{i+1}" not in base:
                        self.e = Label(self.secondCanva, width=10,justify="center", text=f"x{exp[i]}* = 0",
                                        font=('Helvetica',16)) 
                        self.e["bg"] = "#001b2e"
                        self.e["fg"] = "#bbdefb"
                        self.e.grid(row=5, column=column) 
                        column += 1

            elif solution == "unbounded":
                self.e = Label(self.firstCanva, justify="center", text="→ Problema tem solução ilimitada.",
                                    font=('Arial',16)) 
                self.e["bg"] = "#001b2e"
                self.e["fg"] = "#bbdefb"
                self.e.grid(row=0, column=0) 
            elif solution == "endless":
                self.e = Label(self.firstCanva, justify="center", text="→ Problema tem infinitas soluções.",
                                    font=('Arial',16)) 
                                    
                self.e["bg"] = "#001b2e"
                self.e["fg"] = "#bbdefb"
                self.e.grid(row=0, column=0) 

            self.continueButton = Button(self.fourthContainer)
            self.continueButton["text"] = "Novo problema"
            
            self.continueButton["bg"] = "#64b5f6"
            self.continueButton["activebackground"] = "#bbdefb"
            self.continueButton.configure(cursor="hand2")
            self.continueButton["font"] = ("Calibri", "12")
            self.continueButton["width"] = 16
            self.continueButton["command"] = initialScreen
            self.continueButton.pack()

        def initialScreen():
            clearActiveElements()
            self.max = Radiobutton(self.secondContainer, 
            text="Min",
            fg= "#bbdefb",
            bg= "#1b4965",
            activebackground="#bbdefb",
            selectcolor="#001b2e",
            cursor="hand2",
            indicatoron = 0,
            width = 10,
            padx = 10, 
            variable=objProblem, 
            command=objectiveProblem,
            value=0).pack(anchor=W, side=LEFT)

            self.min = Radiobutton(self.secondContainer, 
                text="Max",
                fg= "#bbdefb",
                bg= "#1b4965",
                activebackground="#bbdefb",
                selectcolor="#001b2e",
                cursor="hand2",
                indicatoron = 0,
                width = 10,
                padx = 10, 
                variable=objProblem, 
                command=objectiveProblem,
                value=1).pack(anchor=W, side=LEFT)

            self.variableNumberLabel = Label(self.thirdContainer, text="Número de Variáveis", font=self.standardFont, height=2, bg="#001b2e", fg="#bbdefb")
            self.variableNumberLabel.pack(side=TOP)

            self.variableNumber = Scale(self.thirdContainer)
            self.variableNumber["width"] = 20
            self.variableNumber["orient"] = HORIZONTAL
            self.variableNumber["from_"] = 1
            self.variableNumber["cursor"] = "sb_h_double_arrow"
            self.variableNumber["variable"] = numberVariables
            self.variableNumber["to"] = 9
            self.variableNumber["bg"] = "#001b2e"
            self.variableNumber["fg"] = "#bbdefb"
            self.variableNumber.configure(highlightbackground="#001b2e", highlightcolor="#bbdefb", troughcolor="#294c60", activebackground="#bbdefb", bd=0)
            self.variableNumber.pack(side=TOP)

            self.constraintsNumberLabel = Label(self.fourthContainer, text="Número de Restrições", font=self.standardFont, height=2, bg="#001b2e", fg="#bbdefb")
            self.constraintsNumberLabel.pack(side=TOP)

            self.constraintsNumber = Scale(self.fourthContainer)
            self.constraintsNumber["width"] = 20
            self.constraintsNumber["orient"] = HORIZONTAL
            self.constraintsNumber["from_"] = 1
            self.constraintsNumber["cursor"] = "sb_h_double_arrow"
            self.constraintsNumber["variable"] = numberConstraints
            self.constraintsNumber["to"] = 9
            self.constraintsNumber["bg"] = "#001b2e"
            self.constraintsNumber["fg"] = "#bbdefb"
            self.constraintsNumber.configure(highlightbackground="#001b2e", highlightcolor="#bbdefb", troughcolor="#294c60", activebackground="#bbdefb", bd=0)
            self.constraintsNumber.pack(side=TOP)

            self.continueButton = Button(self.fifthContainer)
            self.continueButton["text"] = "Continuar"
            self.continueButton["font"] = ("Calibri", "12")
            self.continueButton["bg"] = "#64b5f6"
            self.continueButton["activebackground"] = "#bbdefb"
            self.continueButton.configure(cursor="hand2")
            self.continueButton["width"] = 14
            self.continueButton["command"] = modelProblem
            self.continueButton.pack()

        self.standardFont = ("Arial", "11")

        master.configure(background="#001b2e")

        self.firstContainer = Frame(master)
        self.firstContainer["bg"] = "#001b2e"
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["bg"] = "#001b2e"
        self.secondContainer["padx"] = 100
        self.secondContainer["pady"] = 20
        self.secondContainer.pack()
        activeContainers.append(self.secondContainer)

        self.thirdContainer = Frame(master)
        self.thirdContainer["bg"] = "#001b2e"
        self.thirdContainer["padx"] = 80
        self.thirdContainer["pady"] = 20
        self.thirdContainer.pack()
        activeContainers.append(self.thirdContainer)

        self.fourthContainer = Frame(master)
        self.fourthContainer["bg"] = "#001b2e"
        self.fourthContainer["pady"] = 40
        self.fourthContainer.pack()
        activeContainers.append(self.fourthContainer)

        self.fifthContainer = Frame(master)
        self.fifthContainer["bg"] = "#001b2e"
        self.fifthContainer["pady"] = 40
        self.fifthContainer.pack()
        activeContainers.append(self.fifthContainer)

        self.title = Label(self.firstContainer, text="Método Simplex - Fase 2")
        self.title["font"] = ("Arial", "20", "bold")
        self.title["fg"] = "#bbdefb"
        self.title["bg"] = "#001b2e"
        self.title.pack(side=TOP)
        self.title.pack()

        self.objectiveProblem = Label(self.firstContainer, text=f"Objetivo do Problema: Minimizar")
        self.objectiveProblem["font"] = ("Arial", "16")
        self.objectiveProblem["fg"] = "#bbdefb"
        self.objectiveProblem["bg"] = "#001b2e"
        self.objectiveProblem.pack(side=BOTTOM)
        self.objectiveProblem.pack()

        self.problemObjective = Label(self.secondContainer, text="Objetivo do Problema", font=self.standardFont)
        self.problemObjective["width"] = 20
        self.problemObjective["height"] = 2
        self.problemObjective["font"] = self.standardFont
        self.problemObjective.pack(side=TOP)

        initialScreen()


if __name__ == "__main__":
    root = Tk()
    width= root.winfo_screenwidth()  
    height= root.winfo_screenheight() 
    root.geometry("%dx%d" % (width, height)) 
    root.state(newstate="zoomed")
    root.title('Método Simplex')
    Application(root)
    root.mainloop()