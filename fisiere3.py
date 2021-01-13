#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre
#Numărul globuleţelor albe se citeşte din fişierul « globulet.txt »
#Câte globuleţe are brăduţul, ştiind că numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe
#globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii
#Numărul total de globuleţe este înscris în fişierul « bradut.txt »
#Exemplu: Date de intrare: 12 	Date de ieşire: 52.
with open ('globulet.txt','r') as j:
    a=j.readline()
b=int(a)+3
c=int(a)+b-2
s=int(a)+b+c
with open ('bradut.txt','w') as k:
    k.write(str(s))