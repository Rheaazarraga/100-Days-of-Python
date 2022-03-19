# fix this horrendous interpretation of don't stop believin' by Journey

journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

#################################################

# using the replace() method which replaces a specified phrase with another specified phrase
# long way:
# journey = journey.replace("""Just a small tone girl
# Leaving in a lonely whirl
# She took the midnight tray going anywhere
# Just a seedy boy
# Bored and raised in South Detroit or something
# He took the midnight tray going anywhere""", """Just a small town girl
# Living in a lonely world
# She took the midnight train going anywhere
# Just a city boy
# Born and raised in South Detroit
# He took the midnight train going anywhere""")

# print(journey)

# OR - better way:

journey= (journey
.replace("tone", "town")
.replace("Leaving", "Living")
.replace("whirl", "world")
.replace("tray", "train")
.replace("seedy", "city")
.replace("Bored", "born")
.replace(" or something", "")
         )

print(journey)