#Ion şi Vasile joacă următorul joc:
# Ion spune un număr iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
#Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. 
# Ajutaţi-l pe Vasile să găsească răspunsul mai repede
# Din fişierul « input.txt » se citeşte un număr, în fişierul « output.txt » - se înscrie consecutivitatea numerelor.
with open ('input.txt','r') as j:
     a=j.readline()
b=int(a)-2
c=int(a)-1
d=int(a)
e=int(a)+1
f=int(a)+2
with open ('output.txt','w') as k:
    k.write(str(b))
    k.write('\n')
    k.write(str(c))
    k.write('\n')
    k.write(str(d))
    k.write('\n')
    k.write(str(e))
    k.write('\n')
    k.write(str(f))