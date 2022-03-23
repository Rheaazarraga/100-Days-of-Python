# LHL python 21dcc prep work
# Challenge: Word Game/ Mad Libs
# Remember to use:
# Multi-line strings
# User input with `input('...')`
# The `.replace('phrase', 'new phrase')` method
# The humble `print('...')` statement

storyString = """Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME"""

OCCUPATION = input("enter an occupation: ")
COUNTRY = input("enter the name of a country: ")
PLURAL_NOUN = input("enter a plural noun: ")
VERB = input("enter a verb: ")
ADJECTIVE = input("enter a descriptive word: ")
PERSONAL_ITEM = input("now enter a personal item: ")
HOLIDAY = input("enter any holiday of choice: ")
NAME = input("What is your name? ")

storyString = (storyString

               .replace("OCCUPATION", OCCUPATION)
               .replace("COUNTRY", COUNTRY, 2)
               .replace("PLURAL_NOUN", PLURAL_NOUN)
               .replace("VERB", VERB)
               .replace("ADJECTIVE", ADJECTIVE)
               .replace("PERSONAL_ITEM", PERSONAL_ITEM)
               .replace("HOLIDAY", HOLIDAY)
               .replace("NAME", NAME)
               )

print(storyString)