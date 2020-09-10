s = 0
v = 0
for g in range(3,501,3):
    if g % 2 == 1:
        s += g
        v += 1
print(s,v)

# += é igual a x = x+1