# Sea päevane eesmärk (ml)
dailyGoal = 2000
# Sea ühe klaasi maht (ml)
oneGlass = 250
# Küsi mitu klaasi on joodud ja teisenda täisarvuks
amountOfDrinks = int(input("Mitu klaasi sa juba joonud oled?"))
# Kontrolli, kas on joodud vähem kui 50% eesmärgist
if(amountOfDrinks * oneGlass / dailyGoal < 0.5):
    # Anna hoiatus
    print("Joo rohkem vett, keha vajab seda!")
# Kontrolli, kas on joodud 50-99% eesmärgist
elif(amountOfDrinks * oneGlass / dailyGoal < 1):
    # Anna kiitus
    print("Tubli, jätka samas vaimus!")
# Kontrolli, kas on joodud 100% või rohkem
elif(amountOfDrinks * oneGlass / dailyGoal >= 1):
    # Anna suur kiitus
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")