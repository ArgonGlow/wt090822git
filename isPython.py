from xml.etree.ElementInclude import include


#import test.py

print("hello world")

def myFunction():
    print("in function")

myFunction()

class Fiets:
    speed = 0
    price = 220
    
    def fietsen(_self):
        print('fietsen met een snelheid van', _self.speed)

g = Fiets()
f = Fiets()
f.speed = 10

print(f.speed)
print(g.speed)
print(f.fietsen())

