 #[int(i) for i in input().split()]
m = []
while True:
    r = [i for i in input().split()] #[input().split()]
    if 'end' not in r:
        for j in range(0, len(r)):
            r[j] = int(r[j])
        m.append(r)
        print(m)
    if 'end' in r:
        break


    #m.append(int(r))

