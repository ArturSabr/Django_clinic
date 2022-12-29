n,m= [int(i) for i in input().split()]
reisy =[]
for i in range(m):
    reis=[int(i) for i in input().split()]
    reisy.append(reis)
res=[int(i) for i in input().split()]
poryadok=[]
konechka = res[1]
while konechka in [i[1] for i in reisy]:
    poryadok.append([i[1] for i in reisy].index(konechka)+1)
    konechka=reisy[poryadok[-1]-1][0]
print(len(poryadok))
print(*poryadok[::-1])
