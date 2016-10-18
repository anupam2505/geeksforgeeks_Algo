__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 17 / 2016

## Minimum cost problem
def minCostPath(Matrix):
    m = len(Matrix)
    n = len(Matrix[0])
    CM =  [[0 for x in range(n)] for y in range(m)]
    CM[0][0] = Matrix[0][0]
    for i in range(m):
        for j in range(n):
            if i ==0:
                CM[i][j]= Matrix[i][j] + CM[i][j-1]
            elif j ==0:
                CM[i][j]= Matrix[i][j] + CM[i-1][j]
            else:
                CM[i][j] = Matrix[i][j] + min (CM[i][j-1],CM[i-1][j], CM[i-1][j-1] )

    return CM[m-1][n-1]

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCostPath(cost))