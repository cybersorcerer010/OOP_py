"""
This module demonstrates object-oriented programming concepts in Python, 
including class creation, inheritance, encapsulation, and method overriding.

Classes:
    - Superhero: A base class representing a superhero with a name, power, and origin.
    - HeroWithGadget: A subclass of Superhero that introduces a unique gadget.

Example:
    hero1 = Superhero("Thunderbolt", "Lightning Speed", "Sky Realm")
    hero2 = HeroWithGadget("TechBlade", "Technopathy", "Earth", "Energy Sword")
    print(hero1.show_identity())  # Outputs: I am Thunderbolt, with the power of Lightning Speed!
    print(hero2.show_identity())  # Outputs: I am TechBlade, and my gadget is a Energy Sword!
"""

# Parent class: Superhero
class Superhero:
    """Represents a superhero with a name, superpower, and origin."""
    
    def __init__(self, name, power, origin):
        self.name = name  # public attribute
        self._power = power  # protected attribute
        self.__origin = origin  # private attribute
    
    def show_identity(self):
        """Displays the superhero's identity and power."""
        return f"I am {self.name}, with the power of {self._power}!"

    def get_origin(self):
        """Returns the superhero's origin."""
        return self.__origin

# Subclass: HeroWithGadget (inherits from Superhero)
class HeroWithGadget(Superhero):
    """Represents a superhero equipped with a special gadget."""
    
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def show_identity(self):
        """Displays the superhero's identity, overriding the base class method."""
        return f"I am {self.name}, and my gadget is a {self.gadget}!"

# Example objects
hero1 = Superhero("Thunderbolt", "Lightning Speed", "Sky Realm")
hero2 = HeroWithGadget("TechBlade", "Technopathy", "Earth", "Energy Sword")

# Output
print(hero1.show_identity())  # I am Thunderbolt, with the power of Lightning Speed!
print(hero2.show_identity())  # I am TechBlade, and my gadget is a Energy Sword!
print(hero1.get_origin())     # Sky Realm
