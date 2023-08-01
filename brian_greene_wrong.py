import random

'''
At one point, a string theorist named Brian Greene stated:

If you have three balls of two random colors,
that classically the probability of picking two of them of different colors is 1/3,
but that by using quantum mechanics, you could get the probability to be 1/2.

His logic was:

2 of them are guaranteed to be the same color, and the 3rd one has a 1/2 chance of being the same color.
The probability classically is the probability of there being two different colors (1/2)
multiplied by the probability of picking the one with the third color (2/3)
1/2*2/3 = 1/3

Someone else couldn't understand why the probability of there being two different colors wasn't 3/4,
making the math 2/3*3/4=2/4=1/2 

111 112 121 122 211 212 221 222 = 2 all same color, 6 with 1 different color

I could have written this code at that time to understand the truth, but I was overconfident.
I thought that surely Briane Greene, the string theorist was right.
I argued that person's logic was reliant on the balls being in a specific order.
The person pointed out that conflating all of the unordered things still meant 3 unordered : 1 ordered.

Finally, I decided to check what a computer would make of this scenario.
It is possible that I am still wrong, but as you can see, the computer indicates
that both scenarios give a 1/2 ratio of same : different.
'''

# the order of the balls matters
def random_func_1():
    ball_collection = [random.randint(1, 2) for x in range(3)]
    # print(ball_collection, end=' -> ')
    first_ball = ball_collection.pop(random.randint(0, 2)) # this is where the first ball is picked
    second_ball = ball_collection.pop(random.randint(0, 1)) # this is where the second ball is picked
    # print(ball_collection, first_ball, second_ball)
    return first_ball == second_ball


# alternate problem where the order of the balls
# doesn't matter (instead of the balls being picked in an order
# they are picked by ignoring one of the other balls)
def random_func_2():
    ball_collection = [random.randint(1, 2) for x in range(3)]
    # print(ball_collection, end=' -> ')
    non_chosen_ball = random.randint(0, 2) # both chosen balls are picked by ignoring this ball
    chosen_balls = [x for num, x in enumerate(ball_collection) if num != non_chosen_ball]
    # print(chosen_balls, non_chosen_ball)
    return chosen_balls[0] == chosen_balls[1]


if __name__ == "__main__":
    print('Case 1: Order Does Not Matter')
    same_different_dictionary = {'Same': 0, 'Different': 0}
    for _ in range(10000):
        are_same = random_func_2()
        if are_same:
            same_different_dictionary['Same'] += 1
        else:
            same_different_dictionary['Different'] += 1
    print(same_different_dictionary)

    print('Case 2: Order Matters')
    same_different_dictionary = {'Same': 0, 'Different': 0}
    for _ in range(10000):
        are_same = random_func_1()
        if are_same:
            same_different_dictionary['Same'] += 1
        else:
            same_different_dictionary['Different'] += 1
    print(same_different_dictionary)
