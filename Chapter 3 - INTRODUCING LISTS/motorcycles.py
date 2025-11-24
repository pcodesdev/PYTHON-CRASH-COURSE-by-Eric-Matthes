# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)
motorcycles[0] = 'bmw'
print(motorcycles)

# Adding Elements to a List
# Appending Elements to the End of a List
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'bmw')
print(motorcycles)

# Removing Elements from a List
# Removing an Item Using the del Statement
del motorcycles[0]
print(motorcycles)
# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycyle that I owned was a {popped_motorcycle}.")
# Popping Items from Any Position in a List
first_owned_motorcycle = motorcycles.pop(0)
print(f"The first motocycle that I owned was a {first_owned_motorcycle}.")
# Removing an Item by Value
motorcycles.remove("yamaha")
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned_motorcycle = motorcycles[0]

too_old = first_owned_motorcycle
motorcycles.remove(first_owned_motorcycle)

print(f"{too_old.title()} was a very old motorcycle.")
