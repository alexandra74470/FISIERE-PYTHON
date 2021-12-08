f=open('C:\\Users\\User\\Desktop\\Lista_clasei_11D.txt', 'rt')
linii=list(f)
n=0
media=0
print('Nume','\tPrenume','Nota',sep='\t')
for linie in linii:
    campuri=linie.split()
    nota=int(campuri[2])
    n=n+1
    media=media+nota
    print(campuri[0], campuri[1], nota, sep='\t')
    if campuri[3]=='engl.1':
        f=open('C:\\Users\\User\\Desktop\\Grupa_1.txt', 'a')
        f.write(linie)
        f.close()
    else:
        f=open('C:\\Users\\User\\Desktop\\Grupa_2.txt', 'a')
        f.write(linie)
        f.close()
m=round(media/float(n),2)
print('media clasei 11C cu',n,'elevi este', m)
f=open('C:\\Users\\User\\Desktop\\Lista_clasei_11D.txt', 'a')
f.write('\n')
f.write('media clasei:')
f.write(str(m))
f.close()