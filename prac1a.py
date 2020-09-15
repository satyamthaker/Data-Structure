import numpy as np

class list_arr:
    def __init__(self):
        self.l = []

    def adding(self,n):
        self.l.append(n)

    def searching(self,f):
        if f in self.l:
            print("found!!")
        else:
            print("not found")

    def sorting(self):
        self.l.sort()

    def reversing(self):
        self.l = self.l[::-1]

    def display(self):
        print(self.l)
        
def merge():
    a = [1,2, 3, 4, 5, 6, 7]
    b = [8, 9, 10,11,12,13,14]
    merged_list = np.concatenate((a,b))
    return merged_list    
print(merge())

l = list_arr()
l.adding(3)
l.adding(1)
l.adding(4)
l.adding(5)
l.adding(9)
l.adding(8)

l.searching(2)
l.sorting()
l.display()
l.reversing()
l.display()