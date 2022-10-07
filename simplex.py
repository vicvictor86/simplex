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

if __name__ == "__main__":
    initialize()