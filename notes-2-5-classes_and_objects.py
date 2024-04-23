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
          
  # Create a new child class of Pokemon 
class Pikachu(Pokemon): 
  def __init__(self, name ="Pikachu"):
        # call constructor of parent class
        super().__init__()
        
        self.name = name 
        self.id = 25
        self.type = "electric"
        self.actual_cry = "pikachu"
  def thundershock(self,defender: Pokemon)-> str:

    """Simulate a thundershock attack agaist antoehr pokemon
    Params:
    - defender: defending pokemon
    Reutnrs: 
    Str representing result of attack"""
    response = f"{self.name} used thundershock on {defender}"

    if defender.type.lower() in ["water", "flying"]:
        response = response + "it was super effective."
        return response 
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

pikachu_one = Pikachu()
pikachu_two = Pikachu("speedy")

print(pikachu_one.name)
print(pikachu_two.name)
print(pikachu_one.cry())
print(pikachu_two.eat("potion"))

print(pikachu_one.thundershock(pokemon_one))
print(pikachu_two.thundershock(pokemon_two)) 

class Charmander(Pokemon):
    def __init__(self, name= "Charmander"):
        super().__init__()
        self.name = name
        self.id = 133
        self.type = "normal" 
        self.actual_cry = "dannayee"

    def Swift(self, defender: Pokemon) -> str:
       """normal type attack"""
       
       response = f"{self.name} used swift on {defender.name}."

       if defender.type.lower() in ["ghost"]:
            response = response + " It was super effective!"

       elif defender.type.lower() in ["Rock", "steel"]:
            response = response + " It was not very effective."
       
       return response
       
    