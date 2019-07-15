a = str.lower(input())
cnt = 0
for n in a:
    if n == 'g' or n == 'c':
        cnt += 1
d = float(cnt/len(a) * 100)
print(d)
