# Python has several basic data types
text = "Hello"      # string
number = 42         # integer
pi_value = 3.14     # float
is_active = True    # boolean

# Checking types
print(type(text))
print(type(number))
print(type(pi_value))
print(type(is_active))

# Type conversion
num_str = "100"
num_int = int(num_str)  # convert string to int
print(num_int + 50)     # 150

pi_str = str(pi_value)  # convert float to string
print("Pi value is " + pi_str)  # String concatenation
