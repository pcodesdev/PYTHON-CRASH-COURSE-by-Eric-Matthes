# Lists - Python

Lists allow you to store sets of information in one place, whether you have just a few items or millions of items. Lists are one of Python's most powerful features readily accessible to new programmers, and they tie together many important concepts in programming.

## What Is a List?

A **list** is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don't have to be related in any particular way.

In Python, square brackets (`[]`) indicate a list, and individual elements in the list are separated by commas.

**Example:**
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

**Output:**
```
['trek', 'cannondale', 'redline', 'specialized']
```

## Accessing Elements in a List

Lists are ordered collections, so you can access any element in a list by telling Python the position, or **index**, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

**Example:**
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

**Output:**
```
trek
```

The index positions start at 0, not 1. So the first element is at index 0, the second at index 1, and so on.

**Accessing the Last Element:**
Python has a special syntax for accessing the last element in a list. By asking for the item at index `-1`, Python always returns the last item in the list.

**Example:**
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

**Output:**
```
specialized
```

This syntax is quite useful because you'll often want to access the last items in a list without knowing exactly how long the list is. The index `-2` returns the second item from the end of the list, `-3` returns the third item from the end, and so forth.

## Using Individual Values from a List

You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list.

**Example:**
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
```

**Output:**
```
My first bicycle was a Trek.
```

## Modifying, Adding, and Removing Elements

Most lists you create will be dynamic, meaning you'll build a list and then add and remove elements from it as your program runs its course.

### Modifying Elements in a List

The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

**Output:**
```
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

### Adding Elements to a List

You might want to add a new element to a list for many reasons. For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you've built.

#### Appending Elements to the End of a List

The simplest way to add a new element to a list is to **append** the item to the list. When you append an item to a list, the new element is added to the end of the list.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```

**Output:**
```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

The `append()` method makes it easy to build lists dynamically. You can start with an empty list and then add items using a series of `append()` calls.

**Example:**
```python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```

**Output:**
```
['honda', 'yamaha', 'suzuki']
```

#### Inserting Elements into a List

You can add a new element at any position in your list by using the `insert()` method. You do this by specifying the index of the new element and the value of the new item.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
```

**Output:**
```
['ducati', 'honda', 'yamaha', 'suzuki']
```

This operation shifts every other value in the list one position to the right.

### Removing Elements from a List

Often, you'll want to remove an item or a set of items from a list. You can remove an item according to its position in the list or according to its value.

#### Removing an Item Using the del Statement

If you know the position of the item you want to remove from a list, you can use the `del` statement.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```

**Output:**
```
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

You can remove an item from any position in a list using the `del` statement if you know its index.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)
```

**Output:**
```
['honda', 'suzuki']
```

#### Removing an Item Using the pop() Method

Sometimes you'll want to use the value of an item after you remove it from a list. The `pop()` method removes the last item in a list, but it lets you work with that item after removing it.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

**Output:**
```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```

**Practical Use Case:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
```

**Output:**
```
The last motorcycle I owned was a Suzuki.
```

#### Popping Items from Any Position in a List

You can use `pop()` to remove an item from any position in a list by including the index of the item you want to remove in parentheses.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
```

**Output:**
```
The first motorcycle I owned was a Honda.
```

**When to use `del` vs `pop()`:**
- Use `del` when you want to delete an item from a list and not use that item in any way
- Use `pop()` when you want to use an item as you remove it from the list

#### Removing an Item by Value

Sometimes you won't know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the `remove()` method.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```

**Output:**
```
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```

**Practical Use Case:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```

**Output:**
```
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me.
```

**Note:** The `remove()` method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to make sure all occurrences are removed.

## Organizing a List

Often, your lists will be created in an unpredictable order, because you can't always control the order in which your users provide their data. Python provides a number of different ways to organize your lists, depending on the situation.

### Sorting a List Permanently with the sort() Method

Python's `sort()` method makes it relatively easy to sort a list. The `sort()` method changes the order of the list permanently.

**Example (Alphabetical Order):**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

**Output:**
```
['audi', 'bmw', 'subaru', 'toyota']
```

**Example (Reverse Alphabetical Order):**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

**Output:**
```
['toyota', 'subaru', 'bmw', 'audi']
```

**Sorting Temporarily with sorted():**
If you want to maintain the original order of a list but present it in a sorted order, you can use the `sorted()` function.

**Example:**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
```

**Output:**
```
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
```

### Printing a List in Reverse Order

To reverse the original order of a list, you can use the `reverse()` method. Notice that `reverse()` doesn't sort backward alphabetically; it simply reverses the order of the list.

**Example:**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
```

**Output:**
```
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

The `reverse()` method changes the order of a list permanently, but you can revert to the original order anytime by applying `reverse()` to the same list a second time.

### Finding the Length of a List

You can quickly find the length of a list by using the `len()` function. Python counts the items in a list starting with one, so you shouldn't run into any off-by-one errors when determining the length of a list.

**Example:**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
```

**Output:**
```
4
```

This is useful when you need to identify the number of items in a list, work through a list of items, or determine when you've reached the end of a list.

## Avoiding Index Errors When Working with Lists

One type of error is common to see when you're working with lists for the first time. An **index error** occurs when you try to access an item at an index that doesn't exist.

**Example of Index Error:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
```

**Error:**
```
IndexError: list index out of range
```

**Explanation:**
Python attempts to give you the item at index 3, but when it searches the list, no item in `motorcycles` has an index of 3. Because of the off-by-one nature of indexing in lists, this error is typical. People think the third item is item number 3, because they start counting at 1, but in Python the third item is number 2 because it starts indexing at 0.

**Common Mistake with Negative Indices:**
```python
motorcycles = []
print(motorcycles[-1])
```

**Error:**
```
IndexError: list index out of range
```

If an index error occurs and you can't figure out how to resolve it, try printing your list or just printing the length of your list. Your list might look much different than you thought it did, especially if it has been managed dynamically by your program.

**Best Practice:**
Always check if a list is empty or verify the index exists before accessing it:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

# Safe way to access the last element
if motorcycles:
    print(motorcycles[-1])
else:
    print("The list is empty!")
```
