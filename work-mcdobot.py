# McDonald's Bot
# Author: Kaelyn
# February 21 2024 

food = input("Would you like fries with your meal (Yes or no)?")
if food.lower() == "yes":
    print("Here's your meal with fries!")

elif food.lower()== "no":
    print("Here's your meal without fries!")
else: 
    print(f"Sorry I dont understand {food}.")