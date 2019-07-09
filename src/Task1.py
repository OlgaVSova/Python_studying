a = float(input("Print the first number \n"))
b = float(input("Print the second number \n"))
oper = str(input("Print the operation: +, -, /, *, mod, pow, div \n"))

if oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '/' and b != 0.0:
    print(a / b)
elif oper == '/' and b == 0.0:
    print('Деление на 0!')
elif oper == '*':
    print(a * b)
elif oper == 'mod' and b != 0.0:
    print(a % b)
elif oper == 'mod' and b == 0.0:
    print('Деление на 0!')
elif oper == 'pow':
    print(a**b)
elif oper == 'div' and b != 0.0:
    print(a // b)
elif oper == 'div' and b == 0.0:
    print('Деление на 0!')

