import simplex

if __name__ == "__main__":
    tableau = {
        "x1" : [3, 4, -20],
        "x2" : [6, 2, -24],
        "x3" : [1, 0, 0],
        "x4" : [0, 1, 0],
        "b" : [60, 32, 0]
    }
    simplex.base = ["x1", "x4", "x5"]
    while (simplex.testOptimality(tableau) == False):
        simplex.newBaseVariable = simplex.pivoting(tableau)
        tableau = simplex.standardizeTableau(tableau)
    print(tableau)
