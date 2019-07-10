a = int(input())
b = int(input())

counter = 0
d = 0
for n in range(a, b+1):
    if n % 3 == 0:
        counter += 1
        d += n
print(float(d/counter))

