import random

rand_list = [random.randint(0,20) for i in range(10)]

list_comprehension_below_10 = [n for n in rand_list if n<10]


def below_ten(number):
    return number < 10

list_comprehension_below_10 = list(filter(below_ten, rand_list))
