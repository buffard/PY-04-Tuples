# 1. Create a tuple named zoo that contains your favorite animals.
zoo = ("Oshie", "Red Panda", "Lions", "Peacocks")
print(zoo)

# 2. Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("Oshie"))

# another way to do the above
# osh = zoo.index("Oshie")
# print(osh)

# 3. Determine if an animal is in your tuple by using value in tuple.
animal = "donkey"

if animal in zoo:
  print("You know we got that.")
else:
  print("Get out of here")

# 4. Create a variable for each of the animals in your tuple with this cool feature of Python.
# example
# (lizard, fox, mammoth) = zoo
# print(lizard)

(Zero, One, Two, Three) = zoo
print("Show me my 1 index:", One)

# 5. Convert your tuple into a list.
zoo_list = list(zoo)
print(zoo_list)

# 6. Use extend() to add three more animals to your zoo.

add_animals = ["cat", "bats", "rats"]
zoo_list.extend(add_animals)
print(zoo_list)

# 7. Convert the list back into a tuple.

zoo = tuple(zoo_list)
print("new zoo", zoo)