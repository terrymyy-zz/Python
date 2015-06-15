import math
import sys

def is_prime(x):
    '''function that returns whether or not the given number x is prime. returns boolean.'''
    counter = 0
    for i in range(1,x+1):
        if x % i == 0:
            counter += 1
    if counter == 2 :
        return True
    else:
        return False
    
def is_composite(x):
    '''function that returns whether or not the given number x is composite. returns boolean.'''
    counter = 0
    for i in range(1,x+1):
        if x % i == 0:
            counter += 1
    if counter > 2 :
        return True
    else:
        return False
    
def is_perfect(x):
    '''code that returns whether or not the given number x is perfect. returns boolean.'''
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    if sum == x :
        return True
    else:
        return False
    
def is_abundant(x):
    '''code that returns whether or not the given number x is abundant. returns boolean.'''
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    if sum > x :
        return True
    else:
        return False
    
def is_triangular(x):
    '''code that returns whether or not the given number x is triangular. returns boolean.'''
    a,b,c = 1,1,-2*x
    return helper_function(a,b,c)
    
def is_pentagonal(x):
    '''code that returns whether or not the given number x is pentagonal. returns a boolean.'''
    a,b,c = 3,-1,-2*x
    return helper_function(a,b,c)
    
def is_hexagonal(x):
    '''code that returns whether or not the given number x is Hexagonal. returns boolean.'''
    a,b,c = 2,-1,-x
    return helper_function(a,b,c)

def helper_function(a,b,c):
    '''checke if the function has a integer solution or not. returns boolean '''
    i = (-b+(b**2-4*a*c)**0.5)/(2*a)
    return is_int(i)

def is_int(x):
    ''' checks if x is an integer or not. returns boolean '''
    return x == int(x)

def main():
    x = input("Please input a number between 1 and 10000 (enter -1 to exit): \n")
    while x != -1:
        if x > 10000 or x < 1:
            print "Your number is out of range, Please enter again."
            x = input("Please input a number between 1 and 10000 (enter '-1' to exit): \n")
            continue
        print x
        if is_prime(x):
            print " is prime,"
        else:
            print " is not prime,"

        if is_composite(x):
            print " is composite"
        else:
            print " is not composite"

        if is_perfect(x):
            print " is perfect"
        else:
            print " is not perfect"

        if is_abundant(x):
            print " is abundant,"
        else:
            print " is not abundant,"
        
        if is_triangular(x):
            print " is triangular,"
        else:
            print " is not triangular,"
        
        if is_pentagonal(x):
            print " is pentagonal,"
        else:
            print " is not pentagonal,"
        
        if is_hexagonal(x):
            print " is Hexagonal,"
        else:
            print " is not Hexagonal,"

        x = input("Please input a number between 1 and 10000 (enter '-1' to exit): \n")

if __name__ == "__main__":
    main()
