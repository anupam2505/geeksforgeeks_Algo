__Author__ = 'Anupam Panwar'

__Created_On__ = 10 / 22 / 2016


pots = [3,4,7,5]

def maxCoin(pots, start, end):
    if start  > end:
        return 0
    a = pots[start]+min (maxCoin(pots,start+2,end), maxCoin(pots,start+1,end-1))
    b = pots[end]+min (maxCoin(pots,start+1,end-1), maxCoin(pots,start,end-2))

    return max(a,b)

a = maxCoin(pots, 0, 3)
print a