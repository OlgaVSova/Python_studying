maxv, minv = int(input()), int(input())

if minv > maxv:
    tmp = maxv
    maxv = minv
    minv = tmp

lastv = int(input())

if lastv > maxv:
    tmp = maxv
    maxv = lastv
    lastv = tmp

if lastv < minv:
    tmp = minv
    minv = lastv
    lastv = tmp

print(maxv, minv, lastv, sep='\n')
