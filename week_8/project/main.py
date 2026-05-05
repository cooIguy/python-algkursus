from generator import generate_sentence
 


adjectives_path = r"data\adjectives.txt"

animals_path = r"data\animals.txt"

verbs_path = r"data\verbs.txt"


sentence = generate_sentence(adjectives_path, animals_path, verbs_path)

print(sentence)