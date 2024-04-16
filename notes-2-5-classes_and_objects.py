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
        self.actual_cry= "Rooooooooooar!"
        
        
        print("A new Pokemon is born!")
    def cry(self) -> str: 
       return f'{self.name} says, "{self.actual_cry}"'
    
    def eat(self, food: str) -> str:
        """Represents feeding the pokemon 
        ParamL 
        - food: what food you feed it 
        Return: 
        - what it says after consuming it"""
        if food.lower() == "berry":
          return f"{self.name} ate the berry and says \"YUM"
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away."
          
          
        


pokemon_one = Pokemon()
# change its name 
print(pokemon_one.name)
pokemon_one.name = "Pikachu"
print(pokemon_one.name)

pokemon_one.id = 25 
pokemon_one.type = "electric"

print(pokemon_one.id)
print(pokemon_one.type)

pokemon_two = Pokemon()

pokemon_two.name = "Eevee"
pokemon_two.id = 133
pokemon_two.type = "Vaporeon"

print(pokemon_two.name)
print(pokemon_two.id)
print(pokemon_two.type)

pokemon_one.actual_cry = "pikachu"
pokemon_two.actual_cry = "graahh"

print(pokemon_one.cry())
print(pokemon_two.cry())

print(pokemon_one.eat("berry"))
print(pokemon_one.eat("potion"))
print(pokemon_one.eat("poison"))  # mr. ubial does not condone
print(pokemon_two.eat("berry"))
print(pokemon_two.eat("potion"))
print(pokemon_two.eat("poison")) 