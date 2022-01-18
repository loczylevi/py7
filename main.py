'''
2.4 Feladat

A program egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
'''
import random
lista = ["tank","almafa","villámháború","körte","bojler"]
cuccmok = []
tipp = 0
elet = 9
kivalaszt = random.choice(lista)
jovalasz = len(kivalaszt)
print("Gondoltam egy szóra találd ki melyik az!")
print("10 szer probálkozhatsz alapból!")
kerdes = input("Akarod e megváltoztatni az életed számát? (i/n)\t")
if kerdes == "i":
  try:
    elet2 = int(input("Mennyi életed lenne?\t"))
  except:
    print("Számot kértem töki!")
    print("Ha már ilyen vicces hangulatban vagy akkor kevesebb életed lesz! :)")
    elet2 = 2
else:
  elet2 = 9
print(f"Ennyi probálkozásod van akkor alapból: {elet2+1}")
print("________________________________________\n")
while True:
  try:
    bekeres = input("kérek egy betüt!\t")
  except:
    if type(bekeres) != "str":
      print("Betüt kértem töki!")
      elet = 0
      elet2 = 0

  kereso = [szo for szo in kivalaszt if bekeres == szo]
  if elet == 0 or elet2 == 0:
    print(f"Sajnálom elfogytak az életeid Vége a játéknak! A szó amire gondoltam: {kivalaszt}")
    print("<<< GAME OVER >>>")
    break
  if len(kereso) > 0:
    tipp = tipp + 1
    cuccmok.append(bekeres)
    print(f"Helyes! Ez a betű: {bekeres} szerepel a szóban!")
    print(f"Az eltalált szavak: {cuccmok}")
  else:
    print(f"Nem, Ez a betű: {bekeres} NEM szerepel a szóban!")
    elet = elet - 1
    elet2 = elet2 - 1
  if jovalasz == tipp:
    print(f"Eltaláltad! A szó amire gondoltam: {kivalaszt}")
    break

  

