from AuxiliarC import *
from MinRep import *

def main():
    #matrix1 = np.array([[0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]])
    #cliqueM(matrix1)

    #matrix2 = np.array([[1, -1, 1, 1, -1], [-1, 1, -1, 1, 1], [1, -1, 1, -1, 1], [1, 1, -1, 1, -1], [-1, 1, 1, -1, 1]]) #horn-matrix
    #cliqueM(matrix2)

    #matrix3 = np.array([[1, -1, 1, 1, -1], [-1, 1, -1, 1, 1.5], [1, -1, 1, -0.5, 1.5], [1, 1, -0.5, 1, -1], [-1, 1.5, 1.5, -1, 1]]) 
    #cliqueM(matrix3)

    for i in range(5):
        n = np.random.randint(5, 10)
        matrix = radnomCOP(n)
        print(matrix)
        cliqueM(matrix)
main()
