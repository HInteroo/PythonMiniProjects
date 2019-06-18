# Implementation of signed integer class

from copy import copy

class BinInteger(object):
    def __init__(self, n):
        self.n = (n)
        if self.n < -128 or self.n >127:
            raise ValueError("Number must be inbetween -128 and 127:")
        if 0 <= self.n < 128:
            self.rep = makeBinary(self.n)
        elif -128<=self.n<0:
            self.rep = addBinary(onesComplement(makeBinary(self.n)),makeBinary(1))
            
    def decimal(self):
        
        return makeDecimal(self.rep)
       
    def __neg__(self):
        i = addBinary(onesComplement(self.rep),makeBinary(1))
        i.reverse()
        return i
    def __str__(self):
        l = makeBinary(self.n)
        l.reverse()
        return str(l)

    def __add__(self, other):
        summ = addBinary(self.rep,other.rep)
        summ.reverse()
        return summ
        #new = BinInteger(0)
      
        #carry = 0
        #for i in range(8):
         #   new.rep[i], carry = (self.rep[i]+other.rep[i]+carry)%2, (self.rep[i]+other.rep[i]+carry)//2
        #return new

    def __sub__(self, other):
        sub = BinInteger(0)
        l = 0
        for i in range(8):
            sub.rep[i], l = (self.rep[i]-other.rep[i] + l)%2, (self.rep[i]-other.rep[i] + l)//2
        return sub

def addBinary(bitList1, bitList2):
    newList = [0]*8
    carry = 0
    for i in range(8):
        newList[i], carry = (bitList1[i]+bitList2[i]+carry)%2, (bitList1[i]+bitList2[i]+carry)//2
    if (newList[7] == 0 and bitList1[7] == 1 and bitList2[7] == 1):
        raise ValueError("addition overflow")
    if (newList[7] == 1 and bitList1[7] == 0 and bitList2[7] == 0):
        raise ValueError("addition overflow")
    return newList

def onesComplement(bitList):
    newList = [0]*8
    for i in range(8):
        newList[i] = 1 - bitList[i]
    return newList    

def makeBinary(n):
    #precondition: n not negative
    if n < 0:
        raise ValueError('MakeBinary cannot take negative')
    newList = [0]*8
    q = n
    for i in range(8):
        # assign quotient and remainder to be  new q and r
        q, r = q//2, q%2 
        newList[i] = r
    return newList    

def makeDecimal(b):
    #precondition: b not negative
    if b[7] == 1: # binary List is negative if high bit is 1
        raise ValueError('makeDecimal cannot take negative')
    retval = 0
    for i in range(8):
        d = b[i]
        retval = retval + d * 2**i
    return retval
    
if __name__ == "__main__":
    while True:
        try:
            n1 = eval(input("Enter first integer: "))
            b1 = BinInteger(n1)
            print("The opposite of ",str(b1), " is ", str(-b1));
            n2 = eval(input("Enter second integer: "))
            b2 = BinInteger(n2)
            bsum = b1+b2
            bdiff = b1-b2
            print("The sum of ", b1, " and ", b2, " is ", bsum)
            #print("The sum of ", b1.decimal(), " and ", b2.decimal(), " is ", bsum.decimal())
            print("The difference of ", b1, " and ", b2, " is ", bdiff)
            print("The difference of ", b1.decimal(), " and ", b2.decimal(), " is ", bdiff.decimal())
        except ValueError as d:
            print(d)
           
    


    
        






