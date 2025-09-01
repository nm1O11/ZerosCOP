from bron_kerbosch import *
from AuxiliarC import *
from Print import *
from Algorithm_6 import *
from datetime import datetime
import numpy as np

def Graph(COP, J, tau): #J são os vertices da matrix        
    E = set() #E é os pares ordenados 
    for i in J:
        for j in J:
            if i < j:
                if np.isclose(tau[i].T @ COP @ tau[j], 0):
                    E.add((i, j)); E.add((j, i))

    adjM = list()
    for v1 in J:
        adjM.append([1 if (v1, v2) in E else 0 for v2 in J])
    return np.array(adjM)

def cliqueM(COP): # COMO CSV
    start_time = datetime.now()
    J, tau = minZeros(COP)
    adjM = Graph(COP, J, tau)

    if J == set():
        end_time = (datetime.now() - start_time).total_seconds()
        print("Não", end_time)
        #PrintClqE(end_time)
        return list()

    else:
        maxclique = bron_kerbosch(adjM, J)
        end_time = (datetime.now() - start_time).total_seconds()
        print("-->Sim", end_time)
        #PrintClq(maxclique, adjM, time)
        return maxclique