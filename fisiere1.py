#Din fişierul « numere.txt » se citesc două numere
#Afişaţi în fişierul « minim.txt » numărul cel mai mic
# Exemplu : Date de intrare : 44   32   Date de ieşire : 32.
with open ('numere.txt','r') as j:
    a=j.readline()
    b=j.readline()
if int(a)>int(b):
    x=int(b)
if int(b)>int(a):
    x=int(a)
if int(a)==int(b):
    x='numere egale'
with open ('minim.txt','w') as k:
    k.write(str(x))