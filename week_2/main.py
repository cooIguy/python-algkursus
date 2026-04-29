"""
Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal sobiva sõnumi.
Kasutaja sisestab ühe sõna:
"tööpäev"
või "puhkepäev".
Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst:
Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev": kuvatakse ekraanile tekst:
Veel üks osa Netflixist!
"""

tomorrowDay = input("Mis päev on homme? (tööpäev/puhkepäev) ")
if(tomorrowDay == "tööpäev"):
    print("Ma lähen magama, head ööd!")
elif(tomorrowDay == "puhkepäev"):
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus")


#Finantsnõustaja
# Finantsnõustaja
""" Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. 
Selle asemel oled sa palkanud range ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
- küsib, kui palju sul on praegu raha,
- võrdleb seda iPhone 17 Pro hinnaga (näiteks 2 500 €)
- ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. """

print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")
print("Kui palju sul on raha?")
money = int(input("Raha: "))
iPhonePrice = 2500
if(money == iPhonePrice):
    print("Sa võid iPhone 17 Pro osta!")
elif(money > iPhonePrice):
    print("Sa võid iPhone 17 Pro osta! Sul jääb veel " + str(money - iPhonePrice) + " alles!")
else:
    print("Sa ei saa iPhone 17 Pro osta!")
    print("Sa pead veel " + str(iPhonePrice - money) + " eurot koguma!")


#Sammulugeja

"""
Sul on eesmärk teha iga päev 10 000 sammu. Programm küsib kasutajalt, 
mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.

Kui protsent < 50: „Alles poolel teel, liigu edasi!“

Kui protsent < 75: „Tubli, oled peaaegu kohal!“

Kui protsent ≥ 100: „Palju õnne, oled oma eesmärgi täitnud!“
"""
print("Tere tulemast programmi 'Sammulugeja'!")
print("Mitu sammu sa juba täna teinud oled?")
goal = 10000
steps = int(input("Sammud: "))
progress = (steps / goal) * 100

print(f"{progress}%")

if(progress < 50):
    print("Alles poolel teel, liigu edasi!")
elif(progress < 75):
    print("Tubli, oled peaaegu kohal!")
elif(progress < 100):
    print("Oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")