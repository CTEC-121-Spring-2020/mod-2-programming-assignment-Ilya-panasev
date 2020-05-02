'''
CTEC 121
Ilya Panasevich
Module 2 programming assignment
Demonstrate learning and apply functions
'''

''' IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
'''
from math import *

def main():
    '''
    # section 1: Demonstrate assignment statements
    myInt = 25
    myFloat = 10.0
    myString = "completed"

    print(myInt)
    print(myFloat)
    print(myString)
    print()
    
    sum = 70
    print("The sum of 30 and 40 is", sum)
    '''
    '''
    # section 2: Demonstrate the use of the end and sep keywords in print statements
    print("Programming is a very interesting experience", end=".")
    print()
    print("This is an example", "of using sep= to", "separate sections of text", sep="/")
    '''
    '''
    # section 3: Demonstrate the use of the tab, quote and backslash escape characters.
    print("\tThis statement is an example of using the tab escape character")
    print()
    print("\"This statement is supposedly a quote\"")
    print()
    print("This statement demonstrates the usage of \\ (backslash)")
    '''
    '''
    # section 4: Demonstrate getting input from the user (and printing the value obtained back out.)
    myString2 = input("Enter a string of characters or letters:")
    print(myString2)
    print(type(myString2))
    print()
    # int does NOT accept numbers with decimals or letters, must be whole numbers
    myInt2 = int(input("Enter an integer (whole number):"))
    print(myInt2)
    print(type(myInt2))
    print()
    myFloat2 = float(input("Enter a number (decimals are okay):"))
    print(myFloat2)
    print(type(myFloat2))
    print()
    # eval does NOT accept letters. Certain characters, numbers, and decimals are fine. 
    myEval = eval(input("Enter a numeric expression or number:"))
    print(myEval)
    print(type(myEval))
    print()
    '''
    '''
    # section 5: Demonstrate simultaneous assignment
    num1, num2, num3 = 12, 13.4, 15 + 15
    print(num1, num2, num3, sep=", ")
    print()
    varx, vary = eval(input("Enter 2 numbers seperated by a comma:"))
    print(varx, vary, sep=", ")
    '''
    '''
    # section 6: Demonstrate integer arithmetic
    print(5//2)
    print(5%2)
    '''
    '''
    # section 7: Demonstrate definite loops
    for i in [34, 45, 56, 23, 78]:
        print(i)
    print("________")
    for i in range(5):
        print(i)
    print("________")
    for i in range(11, 27, 3):
        print(i)
    '''
    '''
    # section 8: Demonstrate the uses of math imports
    maths1 = 3*pi
    print(maths1)
    print()
    maths2 = sqrt(16)
    print(maths2)
    print()
    maths3 = ceil(4.5)
    print(maths3)
    print()
    maths4 = floor(4.5)
    print(maths4)
    print()
    maths5 = 6**2
    print(maths5)
    print()
    maths6 = 6**3
    print(maths6)
    '''
    '''
    # section 9: Demonstrate the accumulator pattern
    sum = 0
    for i in range(5):
        inputValue = eval(input("Enter a number:"))
        sum = sum + inputValue
    print(sum)
        
    sum = 0
    for i in range(5):
        inputValue2 = eval(input("Enter a number:"))
        sum = sum + inputValue2**2
    print(sum)
    '''
    '''
    # Bonus:
    r = 3
    V = (4/3)*pi*r**3
    print("V =", V)

    r = 3
    A = 4*pi*r**2
    print("A =", A)

    x2 = 6
    x1 = 1
    y2 = 5
    y1 = 2
    slope = (y2 - y1)/(x2 - x1)
    print("slope =", slope)

    a = 1
    b = 2
    c = 3 
    s = (a + b + c)/2
    print("s =", s)

    # problem 5: I had to change a few variables from the original problem because of overlapping variables
    s1 = 1
    a1 = 1
    b1 = 2
    c1 = 3
    A2 = sqrt(s1*(s1 - a1)*(s1 - b1)*(s1 - c1))
    print("A2 =", A2)
    '''

main()   
