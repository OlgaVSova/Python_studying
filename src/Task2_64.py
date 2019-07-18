#элемент равен сумме соседей сверху, снизу, справа и слева
m = []
while True:
    n = [i for i in input().split()]
    if 'end' not in n:
        for j in range(0, len(n)):
            n[j] = int(n[j])
        m.append(n)
    if 'end' in n:
        break
#создать пустой массив такой же размерности и писать в него
cl = len(m) #количество строк
rw = len(m[:][0]) #количество столбцов, длина строки
# print(cl, rw)
# print(m)

if cl == rw == 1:
    print(m[0][0]*4)
elif cl == 1:
    fin = [0 for i in range(0, rw)]
    for r in range(0, -rw, -1):
        for leftright in range(-1, 2, 2):  # число слева и справа от целевого
            fin[r] += m[0][r - leftright] + m[0][r]
    for i in range(0, rw):
        print(fin[i], end = ' ')
    # print(fin)

elif rw == 1:
    fin = [0 for i in range(0, cl)]
    for r in range(0, -cl, -1):
        for updown in range(-1, 2, 2):  #число выше и число ниже целевого
            fin[r] += m[r - updown][0] + m[r][0]
    for i in range(0, cl):
        print(fin[i])
    # print(fin)

else:
    fin = [[0 for i in range(0, rw)] for j in range(0, cl)]
    for c in range(0, -cl, -1):
        for r in range(0, -rw, -1):
            for updown in range(-1, 2, 2): #число выше и число ниже целевого
                # print(fin[c][r])
                # print(updown)
                fin[c][r] += m[c-updown][r]
                # print(m[c-updown][r])
                # print(fin[c][r])
            for leftright in range(-1, 2, 2): #число слева и справа от целевого
                fin[c][r] += m[c][r - leftright]

    for i in range(0, cl):
        for j in range(0, rw):
            print(fin[i][j], end = ' ')
        print("\n", end = '')


