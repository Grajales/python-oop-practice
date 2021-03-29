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
# class Car:
#     def __init__(self,model):
#         self.model = model
     
#     def drive(self):
#         print(f'Vroom Vroom')
        
# class Toyota(Car):
#         def __init__(self,model,color):
#             super().__init__(model)
#             self.color = color
     
           
#         def gasLevel(self,level):
#             self.level=level
#             if self.level=="low":
#                 print(f'fill in your {self.color} {self.model}, its gas tank is {self.level}')
#             elif self.level == "medium":
#                 print(f'your {self.color} {self.model} gas level is {self.level}, it has gas for 150 miles')
#             else: 
#                 print(f'your {self.color} {self.model} gas level is {self.level}, it has gas for 300 miles')
    

            
# mycar2 = Toyota('truck',"green")
# print(mycar2.__dict__)
# # mycar2.drive()
# mycar2.gasLevel('low')
# mycar2.gasLevel('medium')
# mycar2.gasLevel('high')
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
# print(cardsD.__dict__)

# class Card:
#     def __init__ (self):
#         self.suit=['hearts', 'spades','clubs','diamonds']
#         self.rank =['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#         self.score=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# class Deck(Card):
#     def __init__(self):
#         super().__init__(self)
#         self.length=52
#         self.cardDeck=[]
#     def draw(self):
#         for i in range(0,3):
#             for j in range (0,12):
#                 self.cardDeck[i,j]=[self.suit[i],self.rank[j],self.score[j]]
#         return print(f'cardeck {cardDeck}')

# cardsD=Deck()
# print(cardsD.__dict__)
# cardsD.draw
# print(cardsD.draw.__dict__)
# import random
# class Cards:
#     def __init__ (self):
#         self.suit=['hearts', 'spades','clubs','diamonds']
#         self.rank =['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#         self.score=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        
# class Deck(Cards):
#     def __init__(self):
#         super().__init__()
#         self.length = 52
#         self.cardDeck = []
#         self.newCard = []
        
#         for i in range(0,3):
#             for j in range (1,13):
#                 self.cardDeck.append([self.suit[i],self.rank[j],self.score[j]])
#         print(self.cardDeck)
#         print(type(self.cardDeck))
        
#     def draw(self):
#         # random.shuffle(self.cardDeck)
#         # print(self.cardDeck)
#         # self.new_card = self.cardDeck.pop
#         # print(self.new_card)
#         return random.choice(self.cardDeck)
    
#     def pop(self):
#         self.newCard = self.cardDeck.pop(0)
#         print(self.newCard)
    
#     def remove(self):
#         self.newCard = self.cardDeck.pop(0)
#         print(self.newCard)
        

        

# # cardsD = Cards()
# cardsD1 = Deck()
# # print(cardsD1.__dict__)
# print(cardsD1.pop.__dict__)



# class Card:
#     def __init__ (self):
#         self.suit = suit
#         self.rank = rank
#         self.score= score
        
# class Deck():
#     def __init__(self):
#         super().__init__()
#         self.length=52
#         self.cardDeck=[]
#         self.suit=['hearts', 'spades','clubs','diamonds']
#         self.rank =['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#         self.score=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        
#         for i in self.suit:
#             for j in self.score:
#                 #create a card
#                 self.cardDeck.append([self.suit[i],self.rank[j],self.score[j]])

# cardsD = Cards()
# cardsD1 = Deck()
# print(cardsD1.__dict__)



    
    
    
        
