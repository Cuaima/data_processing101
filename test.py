# Chapter 4

# print( "I", "own", "two", "apples", "and", "one", "banana" )
# print ( "I", "own", "two", "apples", "and", "one", "banana" )
# print("I", "own", 2, "apples", "and", 1, "banana")
# print(+1)
# print(1,000,000,000) # 1 0 0 0 -python doesn't use comma sepatators
# print((431 / 100) * 100)
print("hello" + "world")
print(3 * "hello")
print("arrowheads, " * 4 * 4)

# Chapter 5

x = "I would like to purchase that orange inflatable beach"\
    "ball and that small bucket and spade." 
"""
Note that the string assignment of x includes a \. This is a way to concatenate two strings, so it works the same as +. Python convention has a maximum length each line can be, and so do the boxes on this page! This is a way to format a string so it can be (nicely indented to line up visually) on two lines. We’ll get into other examples later.
"""

x = 2
y = 3
print("x =", x)
print("y =", y)
print("x * y =", x * y)
print("x + y =", x + y)

print("x =", x, "and y =", y)  # We now want to swap the values of x and y.
# We do this using a third variable z as an intermediary storage.
z = x
x = y
y = z
print("x =", x, "and y =", y)

# To avoid confusion with capitals and lower case letters, only use lower case letters in variable names. In Python this adheres to the style guidelines.
# If a variable name is chosen that consists of multiple words, put one underscore between each of the words.
# Never choose variable names that start with an underscore. Such variable names are considered reserved for the authors of the Python interpreter.

# It is conventional to always put one space after a # comment, and add two in front if it’s on the same line as code. For example:

# this bit calculates an average
avg = (10 + 5 + 10 + 5) / 4
print("The average is:", avg)  # show the user

"""
<aside>
🤖 **Data Science example**: larger projects with multiple people working on them might have fancy ways of distributing tasks (such as [Slack](https://slack.com), [kanban boards](https://www.atlassian.com/agile/kanban/boards), etc.). A rudimentary way of doing this for yourself is through the use of special comment formats such as

`# TODO: this thing`, `# NOTE: don't break this!`, `# BUG: uh oh it broke`, `#FIXME: please unbreak`. VSCode has extensions (apps) that list these

</aside>
"""