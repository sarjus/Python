d= {'a':1, 'c':20, 'b':5}
temp = list()
for k,v in d.items():
    temp.append((v,k))
print(sorted(temp,reverse=False))
