# classses and objects 

# Big ideas: 
# Classees allow us to couple data and functions together 
# Objects are the actual representation of the classes

# Create a pokemon class; this prepresents a Pokemon 
class Pokemon: # use a capital letter for class name 
    def __init__(self):
        """A special method (function) called the constructor.
          Contains all the properties/variables that descirbe a Pokemon."""
        self.name = ""
        self.id = 0 
        self.weight = 0 
        self.height = 0 
        self.type = "normal"
        
        
        print("A new Pokemon is born!")

# Create two pokemon using our class 
pokemon_one = Pokemon()

# change its name 
print(pokemon_one.name)
pokemon_one.name = "Pikachu"
print(pokemon_one.name) # Pikachu 

pokemon_one.id = 25 
pokemon_one.type = "electric"

print(pokemon_one.id)
print(pokemon_one.type)


pokemon_two = Pokemon()

# change its name 
pokemon_two.name = "Evie"
pokemon_two.id = 4 
pokemon_two.type = "water"

print(pokemon_two.name)
print(pokemon_two.id)
print(pokemon_two.type)
