__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 17 / 2016

def coinchange(arr, N ):
    M = len(arr)
    Matrix = [[0 for i in range(M)] for j in range(N+1)]

    for i in range(N+1):
        for j in range(M):
            if i ==0:
                Matrix[i][j]=1
            else:
                if j-1>=0:
                    x = Matrix[i][j-1]
                else:
                    x =0

                if i-arr[j]>=0:
                    y = Matrix[i-arr[j]][j]
                else:
                    y =0

                Matrix[i][j]=x+y

    return Matrix[N][M-1]


arr = [1, 2, 3]
N = 4
print(coinchange(arr, N ))
