'''
ext2.py
# print anything
print('I could have code like this')
print ("""I wanna a 
burguer""")
'''
'''
ext3.py
print ("I will now count my chickens: ")
print ("Hens"), 25 + 30 / 6
print ("Roosters"), 100 - 25 * 3 % 4
print ("Now I will count the eggs: ")
print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print ("Is it true that 3 + 2 < 5 - 7?")
print (3 + 2 < 5 - 7)
print ("What is 3 + 2?",(3+2))
print ("What is 5 - 7?",(5 - 7))
print ("Oh, that’ s why it’ s False. ")
print ("How about some more. ")
print ("Is it greater?", (5 > -2))
print ("Is it greater or equal?", (5 >= -2))
print ("Is it less or equal?", (5 <= -2))
'''

"""
ext4.py
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available. ")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
"""

'''
ext5.py

my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = "White"
my_hair = "Brown"

print('Let’s talk about. {0}.'.format(my_name))
print("He’s {0} inches tall. ".format(my_height))
print("He’s {0} pounds heavy. ".format(my_height))
print("Actually that’s not too heavy.")
print("He’s got {1} eyes and {0} hair.".format(my_hair,my_eyes))
print("His teeth are usually {0} depending on the coffee.".format(my_teeth,my_name))
# this line is tricky, try to get it exactly right
print("If I add {}, {}, and {} I get {}. ".format(my_age,my_height,my_weight,my_age+my_height+my_weight))
'''


'''
ext6.py
x = "There are {} types of people.".format(10)
binary = "binary"
do_not = "don’ t"
y = "Those who know {} and those who {}".format(binary,do_not)
print(x)
print(y)
print('I said: {}'.format(x))
print('I also said: {}'.format(y))
hilarious = False
joke_evaluation = "Isn’t that joke so funny?!".format(ascii(hilarious))
print(joke_evaluation,"{}".format(hilarious))
w = "This is the left side of... "
e = "a string with a right side."
print (w + e)
'''


'''
ext7.py

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
print(10*"-")
end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"
print(end1+end2+end3+end4+end5+end6+" "+end7+end8+end9+end10+end11+end12)

'''

'''
tabby_cat = "\tI’ m tabbed in."
persian_cat = "I’ m split\non a line."
backslash_cat = "I’ m \\ a \\ cat. "
'''
'''
#fat_cat = '''
#I’ ll do a list:
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
'''
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
'''

'''
ext11.py

print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()
print("So, you’re {} old, {} tall and {} heavy.".format(age,height,weight))

x = input("qual seu nome")
print(x)
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print ("So, you’re {} old, {} tall and {} heavy.".format(age, height, weight))

ext13.py

from sys import argv

script, first, second, third = argv

print('my script is called {}'.format(script))
print('the first variable is {}'.format(first))
print('the second variable is {}'.format(second))
print('the third variable is {}'.format(third))

ext14.py
from sys import argv

script, user_name = argv

prompt = ">"

print("Hi {}, I’ m the {} script.".format(user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me {}?".format(user_name))
likes = input(prompt)
print ("Where do you live {}?".format(user_name))
lives = input(prompt)
print ("What kind of computer do you have?")
computer = input(prompt)
print ("""
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
""".format(likes, lives, computer))


from sys import argv
script, filename = argv
txt = open(filename)

print ("Here’ s your file {}: ".format(filename))
print (txt.read())
print ("Type the filename again: ")
file_again = input("> ")
txt_again = open(file_again)
print (txt_again.read())

'''

from sys import argv
script, filename = argv

print ("We’ re going to erase {}. ".format(filename))
print ("If you don’t want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN. ")
input (" ? ")
print ("Opening the file... ")
target = open(filename,'w')
print ("Truncating the file. Goodbye! ")
target.truncate()

print ("Now I’ m going to ask you for three lines. ")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I’ m going to write these to the file. ")
target.write(line1 )
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print ("And finally, we close it. ")
target.close()



#ext24.py

print("Let’ s practice everything. ")
print("You\’d need to know \’bout escapes with \\ that do \n newlines and \t tabs. ")

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
'''

print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6

print ("This should be five: {}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return int(jelly_beans), int(jars), int(crates)

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print("We’d have {} beans, {} jars, and {} crates. ".format(beans,jars,crates))

start_point = start_point / 10
print("We can also do that this way: ")
print(secret_formula(start_point))
values = (secret_formula(start_point))
#print("We’d have %s beans, %s jars, and %s crates."% (secret_formula(start_point)))
print("We’d have {} beans, {} jars, and {} crates.".format(values[0],values[1],values[2]))


#ext25.py

def break_words(stuff):
    '''This function will break up words for us.'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''Sorts the words.'''
    return sorted(words)

def print_first_word(words):
    '''Prints the first word after popping it off.'''
    word = words.pop(0)
    print (word)

def print_last_word(words):
    '''Prints the last word after popping it off.'''
    word = words.pop(-1 )
    print (word)

def sort_sentence(sentence):
    '''Takes in a full sentence and returns the sorted words.'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''Prints the first and last words of the sentence.'''
    words = break_words(sentence)
    print_first_word (words)
    print_last_word (words)

def print_first_and_last_sorted(sentence):
    '''Sorts the words then prints the first and last one.'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
#ext25-1.py

import ext25

sentence = "All good things come to those who wait."

words = ext25.break_words(sentence)
print(words)

sorted_words = ext25.sort_words(words)
print(sorted_words)

ext25.print_first_word(words)
ext25.print_last_word(words)
print(words)

ext25.print_first_word(sorted_words)
ext25.print_last_word(sorted_words)
print(sorted_words)

sorted_words = ext25.sort_sentence(sentence)
print(sorted_words)

ext25.print_first_and_last(sentence)
ext25.print_first_and_last_sorted(sentence)


#ext26.py

import ext25

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print (word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print (poem)
print ("--------------")

five = 10 + 2 - 3 - 5
print ("This should be five: {}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return int(jelly_beans), int(jars), int(crates)


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print("We'd have {} jeans, {} jars, and {} crates.".format(beans,jars,crates))

start_point = start_point / 10

print("We can also do that this way:")

print("We'd have {} beans, {} jars, and {} crabapples.".format(secret_formula(start_point)[0],secret_formula(start_point)[1],secret_formula(start_point)[2]))

sentence = "All god\tthings come to those who weight."

words = ext25.break_words(sentence)
sorted_words = ext25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ext25.sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)



#ext27.py

True and 1 == 1
False and 0 != 0

True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and (not ("testing" == 1 or 1 == 0))
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))














