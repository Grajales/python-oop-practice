#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:29:05 2021

@author: LG29878
"""

class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname=lastname

    def greet(self):
        print(f'Hi! My name is {self.name} {self.lastname}')

me = User('Liliana','Grajales')
me.greet()
# => "Hi! My name is Jimmy"