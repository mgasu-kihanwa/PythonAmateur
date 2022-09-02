# This is a sample Python script.

# a project of Madlibs (String concatenation)


# some string variable
# print("Please subscribe to " + youtuber)  # a way of adding the value of Youtuber to the print function

# another way is as follows:

# print("Please subscribe to {}".format(youtuber))

# but a more efficient method for remembrance of the variable name is:

# print(f"Please subscribe to {youtuber}")

# ----------------------------------------------------------------------------------------------------------------------
noun = input("Noun: ")
verb1 = input("Verb: ")
game1 = input("First game: ")
game2 = input("Second game: ")
game3 = input("Third game: ")
famousperson = input("Game designer: ")
madlib = f"I hope python will be the best decision I have made for my {noun}. It will definitely have an impact on the \
         job I am {verb1}. I love playing {game1} and {game2} but absolutely despise {game3}. Perhaps {famousperson} \
         can help my experience"

print(madlib)










# See PyCharm help at https://www.jetbrains.com/help/pycharm/
