# More functions 
# Author: Kaelyn 
# 4 April 2024 

def stars(num_stars : int) -> str:
    """Returns a given number of *"""
    return "*" * num_stars
value = ""

if num_stars == 0 or num_stars == 1:
    value = "*"
elif num_stars > 1:
else: 
return value 
# # Multiply Strings 
# greeting = "hello"
# print(greeting * 1_000_000)

# print("The quick brown fox jumps over the laxy dog.")
print(stars(1)) # "*"
print(stars(100))
print(stars(0))
print(stars(-1))
