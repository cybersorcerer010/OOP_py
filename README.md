# OOP_py 🚀

This repository explores key concepts in Python's Object-Oriented Programming (OOP). They focus on designing custom classes, 
implementing inheritance, and leveraging polymorphism to create dynamic and reusable code.

## Table of Contents
- [Design Your Own Class](#design-your-own-class)
- [Polymorphism](#polymorphism-challenge)

---

## Part 1: Design Your Own Class 🏗️

The first part focuses on custom class representing anything you like with the following concepts:
- Creating a class with attributes and methods.
- Using constructors (`__init__`) to initialize object properties.
- Exploring inheritance to extend the functionality of a base class.

### Example Output:
```python
# Creating a superhero
hero = Superhero("Thunderbolt", "Lightning Speed", "Sky Realm")
print(hero.show_identity())  # Output: I am Thunderbolt, with the power of Lightning Speed!
```

## Part 2: Polymorphism 🎭

This activity demonstrates polymorphism by creating a set of classes with the same action (move()), but each class defines 
the action differently. This emphasizes reusability and dynamic method behavior.

### Example Output:
```python
Copy code
# Using polymorphism with vehicles
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
# Output:
# Driving 🚗
# Flying ✈️
# Sailing ⛵
```
