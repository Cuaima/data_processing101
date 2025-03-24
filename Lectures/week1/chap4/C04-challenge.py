"""Exercise 4.1
The cover price of a book is 24.95 EUR, but bookstores get a 40 percent
discount. Shipping costs 3 EUR for the first copy and 75 cents for each
additional copy. Calculate the total wholesale costs for 60 copies."""

# Enter book store code here
copy = 60
cover_price = 24.95 * copy
percent_discount = 40
shipping = (3 - 0.75) + 0.75 * copy

normal_price = cover_price + shipping
discount = (normal_price * percent_discount)/100

print(normal_price - discount)

print(60 * (0.6 * 24.95 + 0.75) + (3 - 0.75) )
print(int(100 * (60 * (0.6 * 24.95 + 0.75) + (3 - 0.75))) / 100)

# -----------------------------------------------------------------------------

"""Exercise 4.2
Can you identify and explain the errors in the following lines of code?
Correct them."""

# Correct the lines of code below:
print("A message")
print("A message")
print('A message')

# -----------------------------------------------------------------------------

"""Exercise 4.3
When something is wrong with your code, Python will raise errors. Often these
will be "syntax errors"  that signal that something is wrong with the form of
your code (e.g., the code in the previous  exercise raised a 'SyntaxError').
There are also "runtime errors", which signal that your code was in itself
formally correct, but that something went wrong during the code's execution.
A good example is the 'ZeroDivisionError', which indicates that you tried to
divide a number by zero (which, as you may know, is not allowed). Try to make
Python raise such a 'ZeroDivisionError'."""

# Enter code that raises a ZeroDivisionError here
# 2/0
# -----------------------------------------------------------------------------

"""Exercise 4.4
Here is another illustrative example of a runtime error. Run the following code
and study the error  that it generates. Can you locate the problem?"""

print(((2 * 3) / 4 + (5 - 6 / 7) * 8))
print(((12 * 13) / 14 + (15 - 16) / 17) * 18)

# -----------------------------------------------------------------------------

"""Exercise 4.5
You look at the clock and see that it is currently 14.00h. You set an alarm to
go off 535 hours later. At what time will the alarm go off? Write a program
that prints the answer. Hint: for the best solution, you will need the modulo
operator. Second hint: The answer is 21.00h, but of course, this exercise is
not about the answer, but about how you get it."""

# Enter clock code here.
day = 24

total = 14 + 535
count_hour = 0
count_day = 0
for hour in range(total):

    count_hour += 1

    if count_hour == 24:
        count_day += 1
        count_hour = 0

print(count_hour)
print(count_day)