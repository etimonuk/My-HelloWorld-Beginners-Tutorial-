
character_name = "Etim"
character_age = "20"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("he really like the name " + character_name + ", ")
print("but didnt like being " + character_age + ".")

print("New\"Man")

phrase = "creator's den"
print(phrase + " is cool")
print(phrase.upper().isupper())
print(phrase[0])
print(phrase.index("n"))
print(phrase.replace("den", "cage"))

print(2 + 4)
print(3 * (4 + 5))

my_num = -15
print(str(my_num) + " my best number")
print(abs(my_num))
print(pow(5, 2))

from math import *
print(floor(2.2))

name = input("Enter your name: ")
print("Hello" + name + "!")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) * float(num2)
print(result)

colour = input("Enter a colour: ")
clothings = input("Enter your clothings: ")
family_member = input("Enter a family member: ")
print("Roses are " + colour)
print("My " + clothings + " is blue")
print("I love my " + family_member)

#list[]' 'list are mutable
friends = ["Onuk", "Etim", "Etetim"]
friends[1] = "Jed"
print(friends[1:])
friends.append("Joyce")
friends.insert(1, "Akpabio")
friends.remove([1])
print(friends)


# tuple()' 'are immutable
coordinates = (4, 5)
print(coordinates[1])
# list of tuple'
coordinates = [(2, 3), (6, 7), (10, 11)]
print(coordinates)

# function; bunch of code line doing one thing to do a task
'1stly "def"'
def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age))

print("Top")
sayhi("Etim", 35)
print("bottom")

# Return function
def cube(num):
    return num*num*num
result = cube(3)
print(result)

# If statement
is_male = True
is_dark = False
if is_male and is_dark:
    print("You are a dark male")
elif is_male and not(is_dark):
    print("you are not a dark male")
elif not is_male and is_dark:
    print("You are a dark female")
else:
    print("You are not a male and not dark")

# If statement and comparison' 'return max number'
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

result = max_num(7, 8, 5)
print(result)

# How to make a calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator!")


# Dictionaries{} is a special structure that allows us to store information in key-value pair
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("jan"))


# While loop is a structre that allows us to loop through and execute a block of code multiple times'
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


# Build a guessing game
secret_word = "onuk"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

# For loop
for letter in "Etim Onuk":
    print(letter)

friends = ["ut", "Etetim", "julz"]
for friend in friends:
    print(friend)

for index in range(5, 10):
    print(index)

friends = ["Etim", "Etetim", "onuk"]
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")


# Exponential function
print(2**3)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4, 2))


# 2D list and nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][2])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)

#Build a translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "2"
        else:
            translation = translation + letter
    return translation

phrase = input("Enter a phrase: ")
print(translate(phrase))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

phrase = input("Enter a phrase: ")
print(translate(phrase))



#Dictionaries{} is a special structure that allows ud to store information in key-value pair'
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions.get("Jan"))


#Try Except block: to manage errors
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("ValueError")

#Reading file
new_school = open("new school.txt", "r")

#print(new_school.readable())
print(new_school.read ())
#print(new_school.readline ())
new_school.close()

#Writing a file
new_school = open("new school.txt", "r")
new_school.read()
new_school.close()

#modules: Import codes from another files
#import filename
#print(filename.variable())

#pips is a package manager use to install modules

#Classes used to store datatypes
from calc import worker

worker1 = worker("Okon","Security", 5, True)
worker2 = worker("Esther", "Catering", 3, False)
worker3 = worker("Dick", "Security", 3, False)

print(worker1.soon_retire())

#Building a multiple question game
from Question import Question
question_prompts = [
    "What colour is Apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour is Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour is Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test (questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")
run_test(questions)

#Inheritance:inherit a function in class into another function

