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

