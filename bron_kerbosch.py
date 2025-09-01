#from datetime import datetime
import numpy as np
from AuxiliarC import *
'''
---utilizar os steps do artigo (1971)
graph - grafo completo (dicionário, keys - vertices, graph[key] - vizinhança (vertices que estão ligados a key))
p - conjunto dos vertices de graph
r, x - conjuntos vazios
cliques - lista vazia (para enumerar os cliques)
'''

def bron_kerbosch(graph, p, r=None, x=None, cliques=None):
    if r is None and x is None and cliques is None: r=set(); x=set(); cliques=list()
    if isinstance(graph, np.ndarray): graph = adj_to_set(graph)
    
    if not p and not x:
        cliques.append(r) #if p and r are both empty sets, then r is a maximal clique (correu todo o grafo)
    else:
        #Step 1. Selection of a candidate.
        for v in p.copy():
            #Step 2. Adding the selected candidate to compsub (r)
            #Step 3. Creating new sets candidates and not from the old sets (p) by removing all points not connected to the selected candidate (to remain consistent with the definition), keeping the old sets in tact.
            #Step 4. Calling the extension operator to operate on the sets just formed.
            bron_kerbosch(graph, p.intersection(graph[v]), r.union({v}), x.intersection(graph[v]), cliques)
            #Step 5. Upon return, removal of the selected candidate from compsub and its addition to the old set not.
            p.remove(v)
            x.add(v)
    return list(map(set, set(frozenset(c) for c in cliques)))