__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 17 / 2016


### bottom up Dynamic programming
def LIS (arr):
    N = len(arr)

    list = [1]*N
    for i in range(1,N):
        for j in range(i):
            if (arr[i]>arr[j] and list[j]>list[i]-1):
                list[i] = 1 + list[j]

    print (max(max(list),1))

arr = [10, 22, 9, 33, 21, 50, 41, 60]
LIS (arr)