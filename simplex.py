from enum import Enum


class modelObjective(Enum):
    max = 1
    min = -1

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

def testOptimality(tableau: dict) -> bool:
    for key in tableau:
        if key != "b":
            if tableau[key][-1] < 0:
                return False
    return True

def pivoting(tableau: dict) -> tuple:
    minValue = 0
    pivotColumn = 0
    pivotLine = 0
    for key in tableau:
        if key != "b":
            if tableau[key][-1] < 0 and tableau[key][-1] < minValue:
                minValue = tableau[key][-1]
                pivotColumn = key
    pivotLine = ratioTest(tableau, pivotColumn)
    return pivotColumn, pivotLine
    

def ratioTest(tableau: dict, pivotColumn) -> int:
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
    return pivotLine

if __name__ == "__main__":
    initialize()