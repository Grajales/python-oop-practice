#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:25:09 2021

@author: LG29878
"""

class BankAccount:
    def __init__(self, type):
        self.type = type
        self.balance=0

    def deposit(self,ammount):
        self.balance=self.balance + ammount
        return self.balance
    
    def widthdraw(self,ammount):
        self.balance=self.balance - ammount
        return self.balance

savings=BankAccount('savings')
checking=BankAccount('checking')
print(checking.deposit(100))
print(checking.widthdraw(20))
print(savings.deposit(10))
print(savings.widthdraw(2))
print(savings.balance)
print(savings.__dict__)
print(checking.__dict__)