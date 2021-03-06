#
# Instructions:
# Work through the following prompts. Prompts marked with "We Do", we will work
# on together, as a class; prompts marked with "You Do", you will be given time
# to work through on your own.
#
# Tip: comment out your solution to each prompt before moving on to the next
# one! This will keep your console clear.
#

#
# Prompt 1: We Do
#
# Define a class for a Car. Your Car class should have the following
# properties:
#
#    - make
#    - model
#    - color
#
# Your Car class should have the following methods:
#
#    - drive: print 'vroom vroom' to the console
#
# Once you create your class definition create two instances.
#********************************************
# ANSWER PROMPT #1
# class Car:
#     def __init__(self,make,model,color):
#         self.make = make
#         self.model =model
#         self.color=color
#     def drive(self):
#         # self.make = make
#         return print('Vroom Vroom')
# mycar = Car('Subaru','Impreza', 'blue')
# print(mycar.__dict__)
# mycar.drive()
#********************************************

# Prompt 2: We Do
#
# We're going to modify our Car class from the previous prompt and extend it to
# create a Toyota class:
#
#   - Extend your Car class to create a Toyota class. The make property will always
#     be 'Toyota'. Add a drive method to your Toyota class.
#
# Make an instance of your Toyota class.
#********************************************
# ANSWER PROMPT #2
# class Car:
#     def __init__(self,model):
#         self.model = model
     
#     def drive(self):
#         print(f'Vroom Vroom')
# class Toyota(Car):
#         def __init__(self,model):
#             super().__init__(model)
            
# mycar2 = Toyota('truck')
# print(mycar2.__dict__)
# mycar2.drive()
#********************************************
#
# Prompt 3: You Do
#
# Define a class for your favorite animal (dog, cat, giraffe, etc). Give your
# class 3 attributes and two methods.
#
# After you've defined your class, create 3 instances.

#********************************************
# ANSWER PROMPT #3
# class Animal:
#     def __init__(self,name,color):
#         self.name= name
#         self.color = color
        

#     def height (self,height):
#         self.height=height
#         return print(f'The {self.name} is {self.color} with a height of {self.height} meters')
    
#     def weight (self,weight):
#         self.weight=weight
#         return print(f'The {self.name} is {self.color} and its weight is {self.weight} kilograms')

# jirafe =Animal('Jirafe','yellow')
# print(jirafe.__dict__)
# jirafe.height(10)
# jirafe.weight(100)
    
#********************************************            
  
    
# Prompt 4: You Do
#
# Once we've completed the above, work through the following changes to your
# Car and Toyota classes:
#
#   - move the color property to your Toyota class
#   - move the drive method to your Car class
#   - add a property to your Toyota class
#   - add a property to your Car class and "fill it in" for your Toyota class

#********************************************
# ANSWER PROMPT #4

#
# Prompt 5: You Do
#
# Define and Animal class with the following properties and methods:
#
#   - group (Invertebrates, Fish, Amphibians, Reptiles, Birds, and Mammals)
#   - eat: log "yum yum" to the console
#   - sleep: log "zzzzz" to the console
#
# Modify your animal from the previous prompt so that it extends your new
# Animal class.
#
# Create an instance of your animal class (the one that extends the Animal
# class).
#
#********************************************
# ANSWER PROMPT #5
#
# Prompt 6: You Do
#
# Define a Card class with the following properties:
#
#   - suit (hearts, spades, clubs, diamonds)
#   - rank (Ace, 2, 3, 4, .. Jack, King, Queen)
#   - score (1, 2, 3, 4, ... 11, 12, 13)
#
# Define a Deck class with the following properties and methods:
#
#   - length (the number of cards - should start at 52)
#   - cards (an array of cards in the deck)
#   - draw: return a random card from the cards array
#
# When you create an instance of your Deck class (i.e. in your constructor),
# fill in the cards array with 52 instances of your Card class. You can do
# this with a nested for loop - first loop through an array of all possible
# suits, then loop through an array of all possible ranks. Inside your inner
# loop, create an instance of your Card class and push it into the Deck's cards
# array.
#
# Instantiate an instance of your Deck and start drawing random cards!
#
