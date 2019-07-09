n = int(input())

if 10 <= n <= 20 or n % 10 == 0 or 11 <= n % 100 <= 14:
    print(n, "программистов")
elif n == 1 or n % 10 == 1:
    print(n, "программист")
elif 2 <= n <= 4 or 2 <= n % 10 <= 4:
    print(n, "программиста")
elif 5 <= n <= 9 or 5 <= n % 10 <= 9:
    print(n, "программистов")

