#Kirjuta programm, mis käib läbi iga tähe sõnes ja prindib selle välja

text = "hello"

# for i in text:
#     print(i)

#Prindi sõna tagurpidi
for letter in range(4, -1, -1):
    print(text[letter])


#Prindi sõna tagurpidi, iga täht kuvatakse eraldi reale
text2 = "C#"
length = len(text2)
print(length)

for letter in range(len(text2) -1, -1, -1):
    print(text2[letter])