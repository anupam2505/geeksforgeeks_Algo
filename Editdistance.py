__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 17 / 2016

def editdistance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    Matrix =  [[0 for x in range(len2+1)] for y in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if (i==0):
                Matrix[i][j]=j
            elif j==0:
                Matrix[i][j]=i
            elif (str1[i-1]==str2[j-1]):
                Matrix[i][j] = Matrix[i-1][j-1]
            else:
                Matrix[i][j] = 1+ min( Matrix[i-1][j-1],  Matrix[i][j-1],  Matrix[i-1][j])
    print(Matrix[len1][len2])

str1 = "sunday"
str2 = "saturday"

editdistance(str1, str2)