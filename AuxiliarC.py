import time
import numpy as np
import math
import cvxpy as cp
import numpy as np

def adj_to_set(graph):
    set_graph = {}
    for line in range(len(graph)):
        set_graph[line] = set([viz for viz in range(len(graph[line])) if graph[line][viz] == 1])
    return set_graph
            
def set_to_adj(graph):
    adj = np.zeros((len(graph), len(graph)))
    for i, line in zip(range(1, len(graph)+1), adj): 
        for l in range(len(graph)): 
            if l+1 in graph[i]: line[l] = 1
    return adj

def comb(n, k):
    if n<k: return 0
    else:
        C = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
        return int(C)
    
def sub_matrix(mainM, subM): #onde subM é um set com o numero das linhas e colunas que queremos
    return(np.array([[mainM[i-1, a-1] for a in subM] for i in subM]))

def project_to_psd(X):
    # Força a matriz a ser simétrica e PSD
    X = 0.5 * (X + X.T)  # Simetriza
    eigvals, eigvecs = np.linalg.eigh(X)
    eigvals[eigvals < 0] = 0  # Zera autovalores negativos
    return eigvecs @ np.diag(eigvals) @ eigvecs.T

def radnomCOP(n):
    while True:
        A = np.random.uniform(-0.5, 0.5, (n, n))
        A = 0.5 * (A + A.T)  # Simetriza
        A = project_to_psd(A)  # Força a ser PSD

        # Adiciona ruído positivo para empurrar em direção à fronteira
        N = np.random.uniform(0, 0.5, (n, n))
        N = np.triu(N, 1)
        N = N + N.T  # matriz com zeros na diagonal, positivos fora
        X = project_to_psd(A+N)

        # Verifica se A é copositiva e perto da fronteira
        x = cp.Variable(n, nonneg=True)
        objective = cp.Minimize(cp.quad_form(x, X))
        constraints = [cp.norm(x, 2) <= 0.01]
        prob = cp.Problem(objective, constraints)
        prob.solve()

        if prob.value is not None and 0 <= prob.value <= 0.001:
            return np.round(A, 2)