# Create a tuple named zoo that contains your favorite animals.
zoo = ("raccoon", "starfish", "armadillo", "cat", "bumblebee")

# Find one of your animals using the .index(value) method on the tuple. 
# Returns the index value
find_specific_animal = zoo.index("armadillo")
# print(find_specific_animal)

# Determine if an animal is in your tuple by using for value in tuple.
for animal in zoo:
	print(animal)

# Create a variable for each of the animals in your tuple with this cool feature of Python.
# example
(raccoon, starfish, armadillo, cat, bumblebee) = zoo
# print(raccoon)

# Convert your tuple into a list. [x]
zoo = list(zoo)
# print(zoo)

# Use extend() to add three more animals to your zoo.
more_animals = ["dog", "kangaroo", "seagull"]
zoo.extend(more_animals)
# print(zoo)

# Convert the list back into a tuple. (x)
zoo = tuple(zoo)
# print(zoo)
