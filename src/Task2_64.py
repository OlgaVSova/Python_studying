 #[int(i) for i in input().split()]
m = []
while True:
    n = [i for i in input().split()] #[input().split()]
    if 'end' not in n:
        for j in range(0, len(n)):
            n[j] = int(n[j])
        m.append(n)
    if 'end' in n:
        break

print(m) #копировать массив и писать в него
cl = len(m)
rw = len(m[:][0])
print(cl, rw)
fin = [[0 for i in range(0, rw)] for j in range(0, cl)]
print(fin)
# for c in range(cl,0, -1):
#     for r in range(rw, 0, -1):
#         #m[c][r]
#         for a in range(c-1, c+1, 2):
#             for b in range(r-1, r+1,2):
#                  m[c][r] += m[a][b]

#элемент равен сумме соседей




    #m.append(int(r))

