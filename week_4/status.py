# Kirjuta Pythoni programm, mis kontrollib kliendi staatust tema kulutuste põhjal.
# Tingimused:
# Kui klient on kulutanud vähemalt 5000 €, siis tema staatus on Platinum.
# Kui klient on kulutanud vähemalt 1000 €, siis staatus on Gold.
# Kui klient on kulutanud vähemalt 500 €, siis staatus on Silver.
# Kui klient on kulutanud vähemalt 100 €, siis staatus on Bronze.
# Kui vähem kui 100 €, siis on ta Tavaline klient.

n = int(input("Palju sa kulutanud oled? (€): "))
# if n >= 5000:
#     print("Platinum")
# elif n >= 1000:
#     print("Gold")
# elif n >= 500:
#     print("Silver")
# elif n >= 100:
#     print("Bronze")
# else: 
#     print("Regular customer")

if n < 100:
    print("Regular customer")
elif n >= 100 and n < 500:
    print("Bronze")
elif n >= 500 and n < 1000:
    print("Silver")
elif n >= 1000 and n < 5000:
    print("Gold")
else:
    print("Platinum")