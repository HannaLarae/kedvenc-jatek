jatekertekek=[]
f=open("játékok.txt", "r", encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    jatekertekek.append(kislista) 
f.close()
#2.feladat
összpontszám=0
for i in range(0, len(jatekertekek)):
    összpontszám=összpontszám+int(jatekertekek[i][1])
print("")
átlagpontszám=összpontszám/len(jatekertekek)
print("1. megoldás: Összesen: "+str(jatekertekek)+" szó található az összes oldalon.")

print
