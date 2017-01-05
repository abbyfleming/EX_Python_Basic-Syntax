''' 
	Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

	Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
	...
'''

showroom = set()

# add(elem) - Add element elem to the set.
showroom.add("Tesla")
showroom.add("Grand Marquis")
showroom.add("Mini Hardtop")
showroom.add("F150")

# print the length
# print(len(showroom))

showroom.add("Tesla")
# print(len(showroom))

# update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs
showroom.update({"Ranger", "Tacoma"})
# print(showroom)

# discard(elem) - Remove element elem from the set if it is present.
showroom.discard("F150")
# print(showroom)

junkyard = set()
junkyard.add("Mini Hardtop")
junkyard.add("Versa")
junkyard.add("Equinox")
junkyard.add("Mustang")
# print(junkyard)

# intersect() - Return a new set with elements common to the set and all others.
common = set(showroom).intersection(junkyard)
# print(common)

#union() - Return a new set with elements from the set and all others.
combine = showroom.union(junkyard)
# print(combine)

#discard()
combine.discard("Mustang")
combine.discard("Versa")
# print(combine)
