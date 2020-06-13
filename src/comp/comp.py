# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [person.name for person in humans if person.name[0]=="D"]
print(a) #### Prints ["Daphne", "David"]

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [person.name for person in humans if person.name[-1]=="e"]
print(b) ### prints ["Alice" "Charlie", "Daphne", "Eve"]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [person.name for person in humans if person.name[0] in ["C", "D", "E", "F", "G"]]
print(c) ### prints ['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David']

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [person.age + 10 for person in humans]
print(d) ### [39, 42, 47, 40, 36, 28, 52, 22, 51, 41]

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [person.name + "-" + str(person.age) for person in humans]
print(e) 
    #['Alice-29', 'Bob-32', 'Charlie-37', 'Daphne-30', 'Eve-26', 'Frank-18', 
    #   'Glenn-42', 'Harrison-12', 'Igon-41', 'David-31']

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(person.name, person.age) for person in humans if person.age in range(27, 33)]
print(f) #[('Alice', 29), ('Bob', 32), ('Daphne', 30), ('David', 31)]

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(person.name.upper(), person.age + 5) for person in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [person.age**0.5 for person in humans]
print(h)
