
# Küsi kasutaja perekonnanime
last_name = input("Mis on sinu perekonnanimi? ")
# Küsi kasutaja sugu
gender = input("Mis on sinu sugu? (m/n) ")
# Kontrolli, kas sugu on 'm'
if(gender == "m"):
    # Tervita meessoost kasutajat
    print("Tere, härra " + last_name)
# Kontrolli, kas sugu on 'n'
elif(gender == "n"):
    # Tervita naissoost kasutajat
    print("Tere, proua " + last_name)
# Muudel juhtudel
else:
    # Tervita üldiselt
    print("Tere tulemast, " + last_name)
