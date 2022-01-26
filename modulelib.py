'''
Author: Kris Gonzalez
DateCreated: 190114
Objective: write tests that execute on a given set of code in order to test
    compatability and give an example of "continuous integration"
'''

def aplusb(a,b):
    return a+b

class Rect:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def perim(self):
        return 2*(self.x+self.y)
    @property
    def area(self):
        return self.x*self.y
    @property
    def diag(self):
        return (self.x**2+self.y**2)**0.5
