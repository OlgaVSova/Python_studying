import time
start_time = time.time()

a = int(input())
b = int(input())
if a == b or a % b == 0:
    print(int(a))
elif b % a == 0:
    print(int(b))
elif a > b:
    d = a % b
    t1 = b
    while d % a != 0 or d % b != 0:
        c = t1 % d
        if c == 0:
            d = a * b / d
            print(int(d))
            break
        t1 = d % c
        if t1 == 0:
            d = a * b / c
            print(int(d))
            break
        d = c % t1
        if d == 0:
            d = a * b / t1
            print(int(d))
            break
else:
    d = b % a
    t1 = a
    while d % a != 0 or d % b != 0:
        c = t1 % d
        if c == 0:
            d = a * b / d
            print(int(d))
            break
        t1 = d % c
        if t1 == 0:
            d = a * b / c
            print(int(d))
            break
        d = c % t1
        if d == 0:
            d = a * b / t1
            print(int(d))
            break

print("time elapsed: {:.10f} ".format(time.time() - start_time))
#{:.2f}s


# elif a > b:
#     d = a
#     while d % a != 0 or d % b !=0:
#         d +=1
#     print(d)
# else:
#     d = b
#     while d % a != 0 or d % b != 0:
#         d += 1
#     print(d)