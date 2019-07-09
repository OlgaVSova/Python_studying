shape = str(input())
if shape == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
elif shape == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a*b
elif shape == 'круг':
    r = float(input())
    S = 3.14*r**2
print(S)

