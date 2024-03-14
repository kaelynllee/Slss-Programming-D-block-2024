# methods (Stirngs
# Author: Kaelyn 
# 21 February 2024

# Ask the use what is the eather like 

weather = input("What's the weather like?")

# If they reply rainy 
    # Bring an umbrella

if weather.lower().strip("!.?, ")== "rainy":
    print("You'll need an umbrella.")
else:
    print(f"Sorry, I don't understand {weather}.")
