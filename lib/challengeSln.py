#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:55:17 2021

@author: LG29878
"""
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

# class Toyota(Car):
#         def __init__(self,model,color):
#             super().__init__('Toyota',model,color)
            
# mycar2 = Toyota('truck','white')
# print(mycar2.__dict__)
# mycar2.drive()


#Another way, but not elegant
# class Toyota(Car):
#         def __init__(self,model,color,make='Toyota'):
#             super().__init__(make,model,color)
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
class Dog:
    def __init__(self,name,breed, owner):
        self.name= name
        self.breed=breed
        self.owner= owner
        
    def play(self):
        print('throw the ball')
    def sleep(self):
        print('ZZZzzzZZZ')
pepper = Dog('Peppermint Mocha',"Collie",'Thiago')
ginger=Dog('Ginger','boxer','Todd')
print(ginger.__dict__)
print(pepper.__dict__)
ginger.play()
pepper.sleep()
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
# class Car:
#     def __init__(self, make, model, mileage):
#         self.make = make
#         self.model =model
#         self.mileage =mileage

#     def drive(self):
#         return print('Vroom Vroom')
    

# class Toyota(Car):
#      def __init__(self,model,color):
#          super().__init__('Toyota',model)
#          self.color = color
#          self.owned = True
#          self.canFly = True
            
# mycar2 = Toyota('truck','white')
# print(mycar2.__dict__)
# mycar2.drive()

#********************************************
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

# class Animal:
#     def __init__(self,name):
#         self.name= name
#     def eat (self):
#         return print('Yum yum')
#     def sleep (self):
#         return print('zzzzz')
    
    
# class Invertebrates(Animal):
#     def __init__(self,name,prey):
#         super().__init__(name)
#         self.prey=prey
#     def eat(self): 
#         print(f'The {self.name} ate a {self.prey}')
#         return super().eat
 
# class Mamals(Animal):
#     def __init__(self,name,prey):
#         super().__init__(name)
#         self.prey=prey
#     def eat(self): 
#         print(f'The {self.name} ate a {self.prey}')
#         return super().eat
        

# dog =Animal("chase")
# dog.eat()
# print(dog.__dict__)
# ant =Invertebrates("ant",'leaf')
# print(ant.__dict__)
# ant.eat()
# Lion =Mamals("Lion",'turkey')
# print(Lion.__dict__)
# Lion.eat()
    
#********************************************     
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

# class Card:
#     global suit, rank, score
#     suit=['hearts', 'spades','clubs','diamonds']
#     rank =['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#     score=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#     def __init__(self):
#         pass
# class Deck(Card):
#     def __init__(self):
#         Card.__init__(self)
#         self.length=52
#         self.cardDeck=[]
#         for i in suit:
#             for j in score:
#                 self.cardDeck.append(self.suit(i),self.rank(j),self.score(j)


# cardsD=Deck()
# print(cardsD.__dict__)

    
    
    
#class Cards: 
#     global suites, values 
#     suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
#     values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
  
#     def __init__(self): 
#         pass
  
  
# # Define a class to categorize each card 
# class Deck(Cards): 
#     def __init__(self): 
#         Cards.__init__(self) 
#         self.mycardset = [] 
#         for n in suites: 
#             for c in values: 
#                 self.mycardset.append((c)+" "+"of"+" "+n) 

# cardsD=Deck()

#Thiago's Solution
class Card:
    def __init__ (self, suit, rank, score):
        self.suit = suit
        self.rank = rank
        self.score = score
class Deck:
    def __init__(self):
        self.length = 52
        self.cards = []
        self.suits= ['hearts', 'spades','clubs','diamonds']
        self.ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.scores = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for suit in self.suits:
            for index, rank in enumerate(self.ranks):
                # create card
                new_card = Card(suit, rank, self.scores[index])
                self.cards.append(new_card)
    def draw(self):
        # how to het the random cards
        new_card = random.choice(self.cards)
        # print('this card is out ===> ', new_card.__dict__)
        self.remove(new_card)
        return new_card
    def pop(self, index):
        self.cards.pop(index)
    def remove(self, card):
        self.cards.remove(card)
deck = Deck()
print(''deck.draw().__dict__)
# list comprehension 
[print(card.__dict__) for  card in deck.cards]