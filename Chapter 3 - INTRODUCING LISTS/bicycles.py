from pyexpat.errors import messages

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Accessing Elements in a List
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
print(bicycles[1].title())
print(bicycles[3].title())

# Python has a special syntax for accessing the last element
# in a list.
print(bicycles[-1].title())

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)