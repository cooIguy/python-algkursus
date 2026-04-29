#Programm palub kasutajal sisestada arvu. Kasutaja sisestab arvu. 
#Programm määrab, kas arv on paaris või paaritu, ja annab vastava tagasiside.

#Modulus (%)

# print(25 % 7)

arv = int(input("Sisesta täisarv: "))

# if arv % 2 == 0:
#     print("Arv on paaris.")
# else:
#     print("Arv on paaritu.")

# #ternary operator
# print("Arv on paaris" if arv % 2 == 0 else "Arv on paaritu")

match arv % 2:
    case 0:
        print("Arv on paaris")
    case 1:
        print("Arv on paaritu")
