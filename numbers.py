import math
import sys

def isPrime(x):
##    function that returns whether or not the given number x is prime.
##    This funtion returns boolean.
    counter = 0
    for i in range(1,x+1):
        if x % i == 0:
            counter += 1
    if counter == 2 :
        return True
    else:
        return False
    
def isComposite(x):
##    function that returns whether or not the given number x is composite.
##    This funtion returns boolean.
    counter = 0
    for i in range(1,x+1):
        if x % i == 0:
            counter += 1
    if counter > 2 :
        return True
    else:
        return False
    return
    
def isPerfect(x):
##    code that returns whether or not the given number x is perfect.
##    This funtion returns boolean.
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    if sum == x :
        return True
    else:
        return False
    
def isAbundant(x):
##    code that returns whether or not the given number x is abundant.
##    This function returns boolean.
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    if sum > x :
        return True
    else:
        return False
    
def isTriangular(x):
##    code that returns whether or not the given number x is triangular.
##    This function returns boolean.
    for i in range(1,x):
        if i*(i+1)/2 == x:
            return True
    return False
    
def isPentagonal(x):
##    code that returns whether or not the given number x is pentagonal.
##    This function returns a boolean.
    for i in range(1,x):
        if i*(3*i-1)/2 == x:
            return True
    return False
    
def isHexagonal(x):
##    code that returns whether or not the given number x is Hexagonal.
##    This function returns boolean.
    for i in range(1,x):
        if 2*i**2 - i == x:
            return True
    return False

def main():
    x = input("Please input a number between 1 and 10000 (enter -1 to exit): \n")
    while x != -1:
        if x > 10000 or x < 1:
            print "Your number is out of range, Please enter again."
            x = input("Please input a number between 1 and 10000 (enter '-1' to exit): \n")
            continue
        print x
        if isPrime(x):
            print " is prime,"
        else:
            print " is not prime,"

        if isComposite(x):
            print " is composite"
        else:
            print " is not composite"

        if isPerfect(x):
            print " is perfect"
        else:
            print " is not perfect"

        if isAbundant(x):
            print " is abundant,"
        else:
            print " is not abundant,"
            pass
        
        if isTriangular(x):
            print " is triangular,"
        else:
            print " is not triangular,"
            pass
        
        if isPentagonal(x):
            print " is pentagonal,"
        else:
            print " is not pentagonal,"
            pass
        
        if isHexagonal(x):
            print " is Hexagonal,"
        else:
            print " is not Hexagonal,"
        pass

        x = input("Please input a number between 1 and 10000 (enter '-1' to exit): \n")
        pass

if __name__ == "__main__":
    main()
