"""
Question 2

A social media influencer wants to increase their followers. They noticed that every time they post a give-away, followers increase by 10%. Naively assuming this goes on forever, they’d like to know how many give-aways to post in order to reach a particular target number of followers.

Parameters: Write a function get_followers which as input takes two arguments:
n_followers : a non-negative int, representing the current number of followers.
t_followers : a non-negative int, representing the target number of followers.

Return: a non-negative int representing the number of give-aways that ensures reaching the target number of followers (assuming the current number of followers as a start).

Example: so,
get_followers(100000,200000)

should return:
8
"""

def get_followers(n_followers, t_followers):

    if n_followers < 0:
        n_followers = n_followers * -1

    if t_followers < 0:
        t_followers = t_followers * -1

    count = 0 

    while n_followers < t_followers:
        ten_percent = n_followers * 10 / 100
        n_followers = n_followers + ten_percent
        count += 1


    return count

print(get_followers(100000,200000))

get_followers(100000,200000)