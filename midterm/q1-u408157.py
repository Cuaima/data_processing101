"""
Question 1


Parameters: Write a function is_palindrome which as input takes a single argument:
input : a str, representing a single sequence of characters.

Return: a bool where True means input is a palindrome and False that it is not.

Note: A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam, racecar or 2002.

Examples: so,
is_palindrome("madam")

Should return:
True
"""

def is_palindrome(word):
    length = len(word)
    word_list = []
    reverse_list = []
    for letter in word:
        word_list.append(letter)
        reverse_list.append(letter)

    reverse_list.reverse()

    if word_list == reverse_list:
        conclusion = True
    else: 
        conclusion = False

    return conclusion

is_palindrome("madam")

# print(is_palindrome("banana"))
# print(is_palindrome("madam"))

