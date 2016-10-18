__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 17 / 2016



def LCS(X,Y,m,n):
    Matrix =  [[0 for x in range(n+1)] for y in range(m+1)]
    i,j=0,0
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                Matrix[i][j]=0
            elif X[i-1]==Y[j-1]:
                Matrix[i][j]=1+ Matrix[i-1][j-1]
            else:
                Matrix[i][j]=max(Matrix[i-1][j], Matrix[i][j-1])

    print Matrix[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
LCS(X,Y,len(X),len(Y))







