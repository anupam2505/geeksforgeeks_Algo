__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 22 / 2016


def isStrobogrammatic(num):
    dic = {'9':'6', '6':'9', '1':'1', '8':'8', '0':'0'}

    l, r = 0, len(num) - 1
    while l <= r:
        if num[l] not in dic or dic[num[l]] != num[r]:
            return False
        l += 1
        r -= 1
    return True

print (isStrobogrammatic("1111179"))
