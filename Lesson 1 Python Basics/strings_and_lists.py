# Strings
greeting = "Hello, Python!"
print(greeting[0])      # First character
print(greeting[-1])     # Last character
print(greeting[0:5])    # Slicing
print(len(greeting))    # Length

# String methods
print(greeting.lower())
print(greeting.upper())
print(greeting.replace("Python", "World"))

# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # First item
print(fruits[-1])  # Last item

# Changing values
fruits[1] = "blueberry"
print(fruits)

# Adding and removing items
fruits.append("orange")
print(fruits)
fruits.remove("apple")
print(fruits)

# List length
print(len(fruits))
