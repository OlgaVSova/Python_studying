lst = [1, 2, 3, 4, 5, 6, 7, 10]


def modify_list(l):
    cnt = 0
    for i in range(0, len(l)):
        if l[i-cnt] % 2 == 0:
            l[i-cnt] = l[i-cnt] // 2
        else:
             del l[i-cnt]
             cnt += 1


modify_list(lst)
print(lst)

