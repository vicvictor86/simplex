import simplex

if __name__ == "__main__":
    tableau = {
        "x1" : [1, 0, 1, -5],
        "x2" : [0, 1, 2, -2],
        "x3" : [1, 0, 0, 0],
        "x4" : [0, 1, 0, 0],
        "x5" : [0, 0, 1, 0],
        "b" : [3, 4, 9, 0]
    }
    simplex.base = ["x1", "x4", "x5"]
    while (simplex.testOptimality(tableau) == False):
        simplex.newBaseVariable = simplex.pivoting(tableau)
        tableau = simplex.standardizeTableau(tableau)
    print(tableau)
    print(simplex.solutionType)
