# Unit 1 Activity
# Author: Kaelyn 
# 4 March 2024


def clean_input(prompt):
    return clean_input(prompt).lower().strip(".,!")
name= input("What's your name?")
print(f" hihihihihi {name}")

drink  = input("What flavour bubble tea do you like (Milk tea or Mango Green tea?")
if drink.lower() == "milk tea":
    print("Here's your 🥛🧋!")
elif drink.lower() == "milk":
    print("Here's your 🥛🧋!")

elif drink.lower()== "mango":
    print("Here's your 🥭🧋!")
elif drink.lower() == "green tea":
    print("Here's your 🥭🧋!")

elif drink.lower() == "mango green tea":
    print("Here's your 🥭🧋!")
else: 
    print(f"Sorry I dont understand {drink}.")