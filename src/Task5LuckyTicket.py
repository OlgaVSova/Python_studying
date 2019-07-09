ticket = str(input())
numbers = int(ticket)
a = numbers // 100000
b = numbers % 100000 // 10000
c = (numbers % 10000) // 1000
d = (numbers % 1000) // 100
e = (numbers % 100) // 10
f = numbers % 10

if a+b+c == d+e+f:
    print("Счастливый")
else:
    print("Обычный")

a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])
d = int(ticket[3])
e = int(ticket[4])
f = int(ticket[5])

print(a, b, c, d, e, f)
if a+b+c == d+e+f:
    print("Счастливый")
else:
    print("Обычный")
