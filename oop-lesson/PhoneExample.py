#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:17:13 2021

@author: LG29878
"""

class Phone:
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print(f"Calling {other_number}.")

    def text(self, other_number, msg):
        print(f"Sending text from {self.number} to {other_number}: {msg}")
        

class IPhone(Phone): #different fro JS where we added "extends", Phone is the parent
    def __init__(self, phone_number):
        super().__init__(phone_number) #referes to the constructor of "Phone"
        self.fingerprint = None

    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == self.fingerprint):
            print("Phone unlocked. Fingerprint matches.")
        else:
            print("Phone locked. Fingerprint doesn't match.")

class Android(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.keyboard = "Default"

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard
        
    def show_keyboard(self):
        print(self.keyboard)
        
        
iphone = IPhone('867-5309')
iphone.set_fingerprint("my thumb")
iphone.call('911')
pexil = Android('234-5678')
pexil.set_keyboard('Funny')
pexil.show_keyboard()
