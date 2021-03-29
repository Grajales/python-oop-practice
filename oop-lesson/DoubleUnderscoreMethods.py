#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:08:49 2021

@author: LG29878
"""

class Dog:
    def __init__(self, name):
        self.name = name
        self.good_dog = True

    def __str__(self):
        return self.name


maddie = Dog('Maddie')
print(str(maddie)) # Maddie
print(maddie) # Maddie
print(maddie.__dict__) # Maddie