lst = [int(i) for i in input().split()]
x = int(input())

if x in lst:
    ind = lst.index(x)
    l = len(lst)
    for i in range(ind, l):
        if lst[i] == x:
            print(i, end=" ")
else:
    print("Отсутствует")
