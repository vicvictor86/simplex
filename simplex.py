from enum import Enum

class modelObjective(Enum):
    max = 1
    min = -1

base = []
newBaseVariable = ("b", -1)
solutionType = ""

def simplex(objectiveFunction, constraints = ""):
    str = separateEquation(objectiveFunction)
    print(str)
    # print(objectiveFunction)
    # print(constraints)
    
def separateEquation(equation):
    list = []
    a = ""
    addVariable = False
    for i in range(0, len(equation)):
        if addVariable:
            a += equation[i]
            list.append(a)  
            addVariable = False
            a = ""
        else:
            a += equation[i]
            if equation[i] == 'x':
                addVariable = True
    return list

def initialize():
    objectiveFunction = getObjectiveFunction()
    # constraints = getConstraints()
    simplex(objectiveFunction)

def getObjectiveFunction():
    return input("Enter the objective function: ").replace(" ", "")

def getConstraints():
    strConstraints = input("Enter the constraints: ")
    constraints = strConstraints.split()
    return constraints

def pivoting(tableau: dict) -> tuple:
    global newBaseVariable
    minValue = 0
    pivotColumn = 0
    pivotLine = 0
    for key in tableau:
        if key != "b":
            if tableau[key][-1] < 0 and tableau[key][-1] < minValue:
                minValue = tableau[key][-1]
                pivotColumn = key
    pivotLine = ratioTest(tableau, pivotColumn)
    base[pivotLine] = pivotColumn
    newBaseVariable = (pivotColumn, pivotLine)
    return pivotColumn, pivotLine

def ratioTest(tableau: dict, pivotColumn) -> int:
    global solutionType
    minRatio = -1
    pivotLine = 0
    for lineIndex in range(len(tableau["b"])):
        try:
            ratio = tableau["b"][lineIndex] / tableau[pivotColumn][lineIndex]
        except ZeroDivisionError:
            ratio = -1
        if ratio > 0 and (ratio < minRatio or minRatio == -1):
            minRatio = ratio
            pivotLine = lineIndex
    if minRatio == -1:
        solutionType = "unbounded"
    return pivotLine

def standardizeTableau(tableau: dict) -> dict:
    global solutionType
    if solutionType == "unbounded":
        return tableau
    lineMultiplier = 1 / tableau[newBaseVariable[0]][newBaseVariable[1]]
    for key in tableau:
        tableau[key][newBaseVariable[1]] *= lineMultiplier
    for lineIndex in range(len(tableau[key])):
        lineMultiplier = - tableau[newBaseVariable[0]][lineIndex] / tableau[newBaseVariable[0]][newBaseVariable[1]]
        if lineIndex != newBaseVariable[1]:    
            for key in tableau:
                tableau[key][lineIndex] += tableau[key][newBaseVariable[1]] * lineMultiplier
    return tableau

def testOptimality(tableau: dict) -> bool:
    global solutionType
    if solutionType == "unbounded":
        return True
    for key in tableau:
        if key != "b":
            if tableau[key][-1] < 0:
                return False
    if checkEndlessSolution(tableau):
        solutionType = "endless"
        return True
    solutionType = "optimal"
    return True

def checkEndlessSolution(tableau: dict) -> bool:
    global solutionType
    for key in tableau:
        if key != "b" and key != newBaseVariable[0]:
            if tableau[key][-1] == 0:
                solutionType = "endless"
                return True
    return False

if __name__ == "__main__":
    initialize()