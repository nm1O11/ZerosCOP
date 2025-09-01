## Print de todos os dados importantes, tal como apresentado no ficheiro Resolts_Ex
import pandas as pd

def printP(COP, P, deltaI, allP, allXP):         
    with open("Resolts.txt", "a") as file:
        file.write(f"\n\nMatrix:")
        for line in COP:
            file.write(f"\n{line}")
        for i in P:
            file.write(f"\n-> delta_I{i}: {deltaI[i]}")
            for j in allP[i]:
                if j==1: file.write(f"\n-> P({i},{j}): {allP[i][j]}")
                else: file.write(f" P({i},{j}): {allP[i][j]}")
            for j in allP[i]:
                if j==1: file.write(f"\n-> X_P({i},{j}): {allXP[i][j]}")
                else: file.write(f" X_P({i},{j}): {allXP[i][j]}")
    return True

def printT(J, tau):
    with open("Resolts.txt", "a") as file:
        file.write(f"\nJ: {J}\nZeros: ")
        for zero in tau:
            file.write(f"{tau[zero]} ")
    return True

def PrintClqE(time):
    with open("Resolts.txt", "a") as file:
        file.write(f"\nA matriz não apresenta nehum zero")
        file.write(f"\nTime: {time} s")

def PrintClq(maxclique, adjM, time):
    with open("Resolts.txt", "a") as file:
        file.write(f"\nTime: {time} s")
        file.write(f"\nMatrix de Adjacencia (formada pelos zeros minimos):")
        for line in adjM:
            file.write(f"\n{line}")
        file.write(f"\nCliques Máximos: {maxclique}")