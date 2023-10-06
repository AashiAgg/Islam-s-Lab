# TODO: write your name and ID below
# Name:Aashi Aggarwal
# ID:8920299


'''def total_price(price, tax):
   
    tp=p+p*(t/100)
    return tp

p= float(input("Enter the price on an Item : "))
t= float(input("Enter the tax % to be paid: "))
print("Final amount to be paid incl. taxes: ",total_price(p,t))'''

'''def divisible_by(x, y):
    if x%y==0:
        return True
    else:
        return False
x=int(input("Enter the number"))
y=int(input("Enter the other number"))
print("Divisibility is ", divisible_by(x,y))'''
'''
def basic_calculator(x, y, operator):
    # TODO: write the functionality of the code where you are
    #  coding a basic calculator that performs basic addition, subtraction,
    #  multiplication, division, modulus and integer division
    #  the function must apply the operator to x and y for example:
    #  basicCalculator(10, 15, "*") should apply 10*15 and save it to the result variable
    #  NOTE: YOU NEED TO HANDLE DIVISION ERRORS BY RETURNING A STRING WITH THE WORD ERROR
    #  NOTE: YOU NEED TO HANDLE AN INVALID OPERATOR BY RETURNING A STRING HAVING THE WORD INVALID
    if (operator=="+"):
        return x+y
    elif (operator=="-"):
        return x-y
    elif (operator=="*"):
        return x*y
    elif (operator=="/" and y!=0):
        return x/y
    elif (operator=="%"):
        return x%y
    elif (operator=="//"):
        return x//y
    else:
        return "Invalid Operator"
x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
o=input("Enter the operator symbol: ")
print(basic_calculator(x,y,o))
'''
'''
def sum_of_even(numbersList):
    # TODO: write the functionality of the code where you are
    # taking as an input a list of numbers
    # returning the sum of even numbers in the list
    # NOTE: YOU NEED TO HANDLE ERRORS OF GIVING LIST OF STRINGS OR STRINGS WITH NUMBERS
    # sum_of_even([1,2,3,4,5,6]) = 12
    return 0


def reverse_string(inputString):
    # TODO: write the functionality of the code where you are
    # taking as an input a string
    # returns the reverse of the string
    # reverse_string("hello") = "olleh"
    return ""


def diamond_string(length):
    # TODO: write the functionality of the code where you are
    # taking as an input a POSITIVE ODD length
    # saves in a string the diamond as follows:
    # diamond_string(5)
    #   *
    #  ***
    # *****
    #  ***
    #   *
    # NOTE: The input must be positive odd, if not return empty string
    return ""


def longest_consecutive_subarray(numberArray):
    # TODO: write the functionality of the code where you are
    # taking as an input an array of numbers
    # return the length of the longest subarray that could be
    # built using the input
    # longest_consecutive_subarray([100, 4, 200, 1, 3, 2]) = 4
    # where the longest_consecutive_subarray that could be built is:
    # [1,2,3,4]
    return 0
'''