# Loops and Iteration 
# Atuhor: Kaelyn 
# 5 April 2024

# Print "something" 10 times
for  _ in range(10):
    print("something")

# Create a grocery list
# Do something for each item in the list
grocery_list = {
    "bubble tea",
    "raspberries",
    "squishamallow",
    "chocolate milk",
    "starbies",
    }

# for every item in the list:
#   *{grocery item}
#   *{grocery item}
#   *{grocery item}
for item in grocery_list:
    if item == "bubble tea":
        print("You can't buy bubble tea!")
        break # STOP LOOPING 
    # skip the rest of the list
    # go directly to bubble tea
 # skip the rest of the list
 # go directly to bubble tea
  
# print the item
    print(f"*{item} ")

for i in range(100):
    print(i +1 )

# This loop repeats indefinitely
while True:
    print("This is an infinite loop.")
# While loops are useful for input validation
# Askl the user if they like ice cream
# If they dont answer yes or no
# Repeat the question

user_answer = input ("Do you like ice cream")
while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input ("Seriously, do you like ice cream?")
if user_answer in ["yes", "yeah"]:
    print("I LOOOOOOOVEEEE ice cream, too!")
if user_answer in  ["no", "nah"]:
    print ("how could you not like ice cream!!")