# #loo lihtne vorm kasutaja andmete kontrollimiseks, kasutajanimi ja parooli kontroll

nimi = input("Sisesta oma nimi: ")
parool = input("Sisesta oma parool: ")

# if nimi == "Mihkel":
#     if parool == "1234":
#         print("Welcome!")
#     else:
#         print("Access denied!") 
# else:
#     print("Access denied!")

# #and

# if nimi == "user" and parool == "1234":
#     print("Welcome!")
# else:
#     print("Access denied!")

#or

if nimi != "user" or parool != "1234":
    print("Welcome!")
else:
    print("Access denied!")