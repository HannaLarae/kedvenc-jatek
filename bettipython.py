
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

print("Az átlagpontszám: "+str(átlagpontszám))
print("Fogok kérni egy pontértéket. Az ennél nagyobb pontszámot elért játékok nevét begyűjtöm egy fájlba, a fájl neve jatékok_pont.txt")
pontérték=int(input("Adja meg a pontértéket!"))

g=open("játékok_pont.txt", "w", encoding="utf-8")
for i in range(0, len(jatekertekek)):
    if int(jatekertekek[i][1])>pontérték:
        g.write(jatekertekek[i][1])
        g.write("\n")

g.close()
#Írja ki a legtöbb és a legkevesebb pontot kapó játék nevét és pontszámát a képernyőre.
