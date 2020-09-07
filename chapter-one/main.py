
## functions
# def my_first_function(str1, str2):
#     print("this is my first string: " + str1)
#     print("and this is the 2nd one: " + str2)
# 
# my_first_function("abc", "xyz")

# default arguments
#def print_something(name = "John Doe", age = "Unknown"):
#    print("my name is:",name, "and my age is:",age)
#
#print_something("eddy", 31)
#print_something("eddy")
#print_something()
#
## using keyword paramters
#print_something(age=31)

# infinite arguments...
#def print_people(*people):
#    for person in people:
#        print("this persion is:", person)
#
#print_people("Nick", "Jack", "Van Damn", "Chuck Norris", "Phil")

# return something from a function
#def do_math(num1, num2):
#    erg = num1 + num2
#    return erg
#
#math1 = do_math(5,7)
#math2 = do_math(11,34)
#
#print(do_math(5,7))
#print(math2)


#if statements
#
#check = "Pommes"
#
#if check == False:
#    print("it is False...")
#elif check == "Hamburger":
#    print("yummi!! Hamburger!")
#elif check == "Pommes":
#    print("yummi - Pommes!")
#else:
#    print("it is true...")


#loopes 
#numbers = [1,2,3,4,5]
#erg = 0
#for number in numbers:
#    print(number)
#    print("summing up...")
#    erg = erg + number
#    print("current sum is:",erg)

#run = True
#current = 1
#
#while run:
#    if current > 100:
#        run = False
#    else:
#        print(current)
#        current += 1

# importing libraries into a script 
#import re

#building a calculator
import re

print("Eddys Calculator")
print("---------------------------")
print("type 'quit' to exit")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:;[]()" "]','', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print("You typed:",previous)

while run:
    perform_math()