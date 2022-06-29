# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 

def hello_USERNAME(user_name):
    print("hello_" + user_name.upper())
hello_USERNAME("eze")

print("\n")

#Question 2 
#Write a Python function, first_odds that prints the odd numbers from 0-100 and returns nothing
def first_odds():
    start, end = 1, 99
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end=" ")
    return None
first_odds()

print("\n")
#Question 3 
#Please write a python function, max_num_in_list to return the max number in a given list. The first line of the code has been defined below.

def max_num_in_list(a_list):
    print("\nThis is the max number in the given list : ", max(num_list))
num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 123456789]
max_num_in_list(num_list)

#Question 4 
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not by 100, unless it's also divisible by 
#400. The result should be a boolean type (true/false)

def is_leap_year(a_year):
     # If a given year is divisible by 4 and also not divisible by 100; it is a leap year (True)
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        leap = True
    #If the given year is divisible by 400; it is a leap year (True)
    elif (a_year % 400 == 0):
        leap = True
    #If the given year is divisible by 100, but not by 400 it is not a leap year (False)
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap = False
    # Any other number that does't meet any of these conditions is not a leap year (False)
    else: 
        leap = False
    return leap
print("\n")
print(is_leap_year(1940))

#Question 5 
#Write a function to check to see if all numbers in a list are consecutive numbers. For example, [2, 3, 4, 5, 6, 7] are consecutive, but 
#[1,2,4,5] are notconsecutive numbers. The return should be boolean type. 

def is_consecutive(a_list):
    if len(set(a_list)) == len(a_list) and max (a_list) - min(a_list) == len(a_list) -1:
        return True
    else:
        return False

number_list = [1,2,3,4,5,6,7]

print("\n")
print(is_consecutive(number_list))


