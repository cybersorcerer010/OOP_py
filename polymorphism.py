"""
This module demonstrates polymorphism in Python using a Vehicle class hierarchy.

Classes:
    - Vehicle: A base class representing a generic vehicle.
    - Car: A subclass of Vehicle representing a car that moves by driving.
    - Plane: A subclass of Vehicle representing a plane that moves by flying.
    - Boat: A subclass of Vehicle representing a boat that moves by sailing.

Example:
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        print(vehicle.move())
    # Output:
    # Driving 🚗
    # Flying ✈️
    # Sailing ⛵
"""

# Parent class: Vehicle
class Vehicle:
    """Represents a generic vehicle with a move method to be defined by subclasses."""    
    def move(self):
        """Defines how the vehicle moves. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass: Car
class Car(Vehicle):
    """Represents a car that moves by driving."""  
    def move(self):
        """Returns the movement method for a car."""
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    """Represents a plane that moves by flying."""
    def move(self):
        """Returns the movement method for a plane."""
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    """Represents a boat that moves by sailing."""
    def move(self):
        """Returns the movement method for a boat."""
        return "Sailing ⛵"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
