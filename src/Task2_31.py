a = int(input())
b = int(input())
c = int(input())
d = int(input())

for n in range(c, d+1):
    print("\t", n, end="")

for n in range(a, b+1):
    print("\n", end="")
    print(n, end="")
    for m in range(c, d+1):
        print("\t", n*m, end="")

