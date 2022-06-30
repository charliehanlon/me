"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# This is a list
some_words = ["what", "does", "this", "line", "do", "?"]
...
# I think this will print all the terms listed in some_words.
for word in some_words: 
    print(word) #it printed all the terms individually.
...
# Something different to "word"
for x in some_words:
    print(x) #it printed all the terms individually, same as "word".
...
#it will print the whole line.
print(some_words) #it printed the whole "[]"
...
# it will print to say more than 3.
if len(some_words) > 3:
    print("some_words contains more than 3 words") # it printed the "(xxx)"


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
