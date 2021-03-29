#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Liliana's version
"""
Created on Fri Mar  5 14:11:21 2021

@author: LG29878
"""
class BankAccount:
    def __init__(self):
        self.balance=0
        self.interest_rate =0.02
        
        
    def check_balance(self):
        return self.balance

    def deposit(self,ammount):
        if ammount <0:
            return False
        self.balance=self.balance + ammount
        #another option self.balance += ammount
        return self.balance
    
    def widthdraw(self,ammount):
        if ammount <0:
            return False
        self.balance = self.balance - ammount
        return self.balance
   
    def accumulate_interest(self):
        self.balance = self.balance + (self.balance * interest_rate)
        return self.balance


class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate =0.02

    def accumulate_interest(self):
        self.balance = self.balance + 10
        return self.balance
        
class OverdraftAccount(BankAccount):
        def __init__(self):
        super().__init__()
        self.overdraft_penalty = 40
        
        def accumulate_interest(self):
            if self.balance<0:
                return False
            return super().accumulate_interest
        
        def widthdraw(self,ammount):
            if self.balance <ammount:
                self.balance = self.balance - self.overdraft_penalty
                return False
            return super().widthdraw(ammount)
            

