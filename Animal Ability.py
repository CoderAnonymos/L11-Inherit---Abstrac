from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):

    def move(self):
        
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        
        print("I can crawl and slither")

class Dog(Animal):

    def move(self):
        
        print("I can walk and run and roll")

class Lion(Animal):

    def move(self):
        
        print("I can walk and run and sneak and prowl and pounce")

h =  Human()

h.move()

s =  Snake()

s.move()

d =  Dog()

d.move()

l = Lion()

l.move()