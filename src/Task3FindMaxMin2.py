a, b, c = int(input()), int(input()), int(input())
maxv = a
minv = b

if b > a:
    maxv = b
    minv = a

if c > maxv:
    maxv = c

if c < minv:
    minv = c

lastv = a+b+c-maxv-minv

print(maxv, minv, lastv, sep='\n')