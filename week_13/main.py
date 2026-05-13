from animal import Animal, Cat, Dog

my_cat = Cat("Fluffy")
my_dog = Dog("Blacky")

neighbours_dog = Dog("Villu")
my_cat.cat_sees(neighbours_dog)
my_dog.dog_sees(my_cat)