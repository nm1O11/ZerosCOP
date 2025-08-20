from bron_kerbosch import *
from AuxiliarC import *
from Algorithm_6 import *
from datetime import datetime
import numpy as np
import scipy as sc

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
    return J, np.array(adjM)

#def cliqueM(COP):         COMO TXT
#    start_time = datetime.now()
#    J, tau = minZeros(COP)
#    J, adjM = Graph(COP, J, tau)
#    if J == set():
#        end_time = (datetime.now() - start_time).total_seconds()
#        with open("Resolts.txt", "a") as file:
#            file.write(f"\nA matriz não apresenta nehum zero")
#            file.write(f"\nTime: {end_time} s")
#        return list()

#    else:    
#        maxclique = bron_kerbosch(adjM, J)
#        end_time = (datetime.now() - start_time).total_seconds()
#        with open("Resolts.txt", "a") as file:
#            file.write(f"\nTime: {end_time} s")
#            file.write(f"\nMatrix de Adjacencia (formada pelos zeros minimos):")
#            for line in adjM:
#                file.write(f"\n{line}")
#            file.write(f"\nCliques Máximos: {maxclique}")
#        return maxclique
    
def cliqueM(COP, writer=pd.ExcelWriter("resultados.xlsx", engine="openpyxl")): # COMO CSV
    start_time = datetime.now()
    J, tau = minZeros(COP)
    J, adjM = Graph(COP, J, tau)

    if J == set():
        print("Não")
        end_time = (datetime.now() - start_time).total_seconds()
        #df_result = pd.DataFrame([["A matriz não apresenta nenhum zero"], ["Tempo (s)", end_time]])
        #df_result.to_excel(writer, sheet_name="Clique", index=False, header=False)
        return list()

    else:
        print("--> Sim")
        maxclique = bron_kerbosch(adjM, J)
        end_time = (datetime.now() - start_time).total_seconds()

        #df_time = pd.DataFrame([["Tempo (s)", end_time]])
        #df_time.to_excel(writer, sheet_name="Clique", startrow=0, index=False, header=False)

        #df_adjM = pd.DataFrame(adjM)
        #df_adjM.to_excel(writer, sheet_name="Clique", startrow=3, index=False)

        #df_cliques = pd.DataFrame([list(clique) for clique in maxclique])
        #df_cliques.to_excel(writer, sheet_name="Cliques", index=False)

        return maxclique