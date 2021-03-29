#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#NOT WORKING, See in class example
"""
Created on Fri Mar  5 10:59:14 2021

@author: LG29878
"""

class BankAccount:
    def __init__(self, acc_type, method, balance):
        self.method = method
        self.acc_type = acc_type
        self.balance = int(balance)

    def checking(self):
        print('Hi!  you are in checking')
        
        
    def savings(self):
        print('Hi! you are in savings')
    
    
    def BankActivity(self):
        if self.acc_type =='savings':
            savings()
        else:
            checking() 
    
    def Balance(self):
        if method==widthdraw:
            balance=balance-moneyAmount
        elif method==save:
            balance=balance+moneyAmount
    BankActivity()

me = BankAccount('savings',"withdraw",0)
