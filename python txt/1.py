a = ['100117A','100702A','111020A.xalsx','120804A','140903A','141212A','150423A','150710A','180727A']
a1 = [[] for _ in range(len(a))]
a2 = [[] for _ in range(len(a))]
for r in range(0, len(a)):
    a1[r] = a[r]+'.xlsx'
    a2[r] = a[r]+'.txt'
print(a1,a2)