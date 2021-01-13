#Se dau două numere
#Să se înmulţească cel mai mare cu doi şi cel mai mic cu trei şi să se afişeze rezultatele
#Exemplu : date de intrare « numere.txt »: 3  7  date de ieşire « produs.txt »: 9  14
with open ('numere.txt','r') as j:
    a=j.readline()
    b=j.readline()
if int(a)>int(b):
    x=int(a)*2
    y=int(b)*3
if int(b)>int(a):
    x=int(b)*2
    y=int(a)*3
if int(a)==int(b):
    x='numere egale'
with open ('produs.txt','w') as k:
    k.write(str(x))
    k.write('\n')
    k.write(str(y))