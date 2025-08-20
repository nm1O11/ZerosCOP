from AuxiliarC import *
from MinRep import *

def main():
    #matrix1 = np.array([[0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]])
    #print(cliqueM(matrix1))

    #matrix2 = np.array([[1, -1, 1, 1, -1], [-1, 1, -1, 1, 1], [1, -1, 1, -1, 1], [1, 1, -1, 1, -1], [-1, 1, 1, -1, 1]]) #horn-matrix
    #print(cliqueM(matrix2))

    #matrix3 = np.array([[1, -1, 1, 1, -1], [-1, 1, -1, 1, 1.5], [1, -1, 1, -0.5, 1.5], [1, 1, -0.5, 1, -1], [-1, 1.5, 1.5, -1, 1]]) 
    #print(cliqueM(matrix3))

    for i in range(100):
        n = np.random.randint(10, 20)
        matrix = radnomCOP(n)
        cliqueM(matrix)
main()