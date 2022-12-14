from enum import Enum

from numpy import identity

class modelObjective(Enum):
    max = 1
    min = -1

base = []
newBaseVariable = ("b", -1)
solutionType = ""

def identityMatrix(dim):
    matrix = []
    for i in range(dim):
        matrix.append([])
        for j in range(dim):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix

def initializeBaseVariables(tableau: dict):
    filledBase = [False] * (len(tableau["b"]) - 1)
    identity = identityMatrix(len(tableau["b"]) - 1)
    for key in tableau:
        if key != "b":
            for i in range(len(tableau["b"]) - 1):
                if tableau[key][:len(tableau["b"]) - 1] == identity[i] and filledBase[i] == False:
                    base.append(key)
                    filledBase[i] = True

def simplex(tableau: dict):
    finalTableau = tableau
    initializeBaseVariables(finalTableau)
    while (testOptimality(finalTableau) == False):
        newBaseVariable = pivoting(finalTableau)
        finalTableau = standardizeTableau(finalTableau)
    return finalTableau, solutionType

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
        if key != "b" and key not in base:
            if tableau[key][-1] == 0:
                solutionType = "endless"
                return True
    return False

if __name__ == "__main__":
    tableau = {
        "x1" : [1, 0, 1, -5],
        "x2" : [0, 1, 2, -2],
        "x3" : [1, 0, 0, 0],
        "x4" : [0, 1, 0, 0],
        "x5" : [0, 0, 1, 0],
        "b" : [3, 4, 9, 0]
    }

    tableauSol, solution = simplex(tableau)
    print(tableau)
    print(solution)
    