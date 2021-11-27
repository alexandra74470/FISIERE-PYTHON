f=open('c:/Users/user/Desktop/input.txt','w')
text=input('textul fisierului:')
f.write(text)
f.close()
f=open('c:/Users/user/Desktop/input.txt', 'r')
a=f.read()
v=[]
n=0
for i in a:
    if (i=='A') or (i=='a') or (i=='E') or (i=='e') or (i=='I') or (i=='i') or (i=='O') or (i=='o') or (i=='U') or (i=='u'):
        v+=i
        n+=1
f.close()
f=open('c:/Users/user/Desktop/vocale.txt','a')
f.write(str(v))
f.write('\n')
f.write('numarul de vocale:')
f.write(str(n))
f.close()