#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Liliana's version
"""
Created on Fri Mar  5 14:11:21 2021

@author: LG29878
"""
class BankAccount:
    def __init__(self, type):
        self.type = type
        self.balance=0
        self.interest_rate =0.02
        self.overdraft_fees = 0

    def deposit(self,ammount):
        self.balance=self.balance + ammount
        return self.balance
    
    def widthdraw(self,ammount):
        self.balance=self.balance - ammount
        return self.balance'
   
    def accumulate_interest(self,interest):
        self.balance= self.balance + (self.balance * interest)
        

class ChildrensAccount(BankAccount()):
    def __init__(self, type):
        super().__init__(type) 
        self.balance = balance
    def accumulate_interest(self, fix_ammount):
        self.balance = self.balance + fix_ammount
        
class OverdraftAccount(BankAccount()):
        def __init__(self, type):
        super().__init__(type)
        def overdraft_penalty:
            if  self.balance - ammount <0:
            self.overdraft_fees=self.overdraft_fees + 40
    


savings=BankAccount('savings')
checking=BankAccount('checking')
print(checking.deposit(100))
print(checking.widthdraw(20))
print(savings.deposit(10))
print(savings.widthdraw(20))
print(savings.balance)
print(savings.__dict__)
print(checking.__dict__)