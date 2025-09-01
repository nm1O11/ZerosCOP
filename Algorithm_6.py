# Algorithm for constricting the set P(j) contain in P, j in V.
from AuxiliarC import *
from Print import *
from itertools import combinations
import numpy as np
import scipy as sc

def condA(P, COP): #rank(COP(P)) = |P|-1
    COP_P = sub_matrix(COP, P)
    return np.linalg.matrix_rank(COP_P) == len(P)-1

def condB(P, COP): # E t(P): COP(P)t(P) = 0, t(P)>0, ||t(P)||1 = 1
    COP_P = sub_matrix(COP, P)
    null_space = sc.linalg.null_space(COP_P) 
    if null_space.shape[1] != 1:
        return False
    tP = null_space[:, 0]
    if np.all(tP > 0):
        return True
    elif np.all(tP < 0):
        tP = -tP
        return True
    else: return False

def findP(COP):
    #STEP 1
    p = len(COP)
    P = {i+1 for i in range(p)} # P = {1, ..., p}
    deltaI = dict(); I = dict(); allP = dict(); allXP = dict(); Iline = dict()

    deltaI[1] = {k for k in P if COP[k-1,k-1] == 0}
    allP[1] = dict(); allXP[1] = dict()
    if deltaI[1] != set():
        for i in deltaI[1]:
            allP[1][i] = {i}; allXP[1][i] = np.eye(p)[i-1]
        L = {i for i in P if i not in deltaI[1]} #L contido em P
    else: L = P 
    
    #STEP 2, ..., p
    for step in range(2, p+1):
        I[step] = {i for i in range(1, comb(len(L), step)+1)} #lista de 1 a c, c o máximo de combinações(len(L), step), ex: C(4, 2), L={1,2,3,5}, step=2
        allP[step] = dict(); allXP[step] = dict()
        c = list(combinations(L, step)) #lista de combinações
        for i in I[step]:
            allP[step][i] = {el for el in c[i-1]} #set dos elementos presentes na combinação (el pertence a L)
            allXP[step][i] = np.array([1 if a in c[i-1] else 0 for a in P]) 

        if step == 2:
            deltaI[step] = {i for i in I[step] if condA(allP[step][i], COP) and condB(allP[step][i], COP)} #deltaI é conjunto

        if step >= 3: 
            if I[step] == set():
                Iline[step] = {}
            else:
                Iline[step] = set()
                for m in range(2, step):
                    for j in deltaI[m]:
                        Iline[step] = {i for i in I[step] if np.dot(np.ravel(allXP[step][i]), np.ravel(allXP[m][j])) < m}
            deltaI[step] = {i for i in Iline[step] if condA(allP[step][i], COP) and condB(allP[step][i], COP)}

    #printP(COP, P, deltaI, allP, allXP)
    return P, deltaI, allXP

def findTau(deltaI, allXP):
    J = {i for i in range(91, sum([len(deltaI[i]) for i in deltaI if deltaI[i]!=set()])+1)}
    tau = dict(); 

    if J == set():
        printT(J, tau)
        return J, tau 
    
    index = 1
    for i in deltaI:
        for j in deltaI[i]:
            tau[index] = allXP[i][j] / np.linalg.norm(allXP[i][j], ord=1)
            index += 1
    
    #printT(J, tau)
    return J, tau

def minZeros(COP):
    P, deltaI, allXP = findP(COP)
    J, tau = findTau(deltaI, allXP)
    return J, tau