# Python List Comprehension
old_list = [int(num) for num in input().split()]

binary_list = [x * 0 if x <= 0 else 1 for x in old_list]
print(binary_list)





# Python's list slice syntax can be used without indices
# for a few fun and useful things:

# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
lst
# []

# You can replace all elements of a list
# without creating a new list object:
a = lst
lst[:] = [7, 8, 9]
lst
# [7, 8, 9]
a
# [7, 8, 9]
a is lst
# True

# You can also create a (shallow) copy of a list:
b = lst[:]
b
# [7, 8, 9]
b is lst
# False


# Python has a HTTP server built into the
# standard library. This is super handy for
# previewing websites.

# Python 3.x
# $ python3 -m http.server

# Python 2.x
# $ python -m SimpleHTTPServer 8000

# (This will serve the current directory at
#  http://localhost:8000)

# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(calc_operator, x, y):
    if calc_operator == 'add':
        return x + y
    elif calc_operator == 'sub':
        return x - y
    elif calc_operator == 'mul':
        return x * y
    elif calc_operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(calc_operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(calc_operator, lambda: None)()


dispatch_if('mul', 2, 8)
# 16

dispatch_dict('mul', 2, 8)
# 16

dispatch_if('unknown', 2, 8)
# None

dispatch_dict('unknown', 2, 8)
# None


# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myfunc(a, b):
    return a + b

funcs = [myfunc]

funcs[0]

# <function myfunc at 0x107012230>
funcs[0](2, 3)
#5



# "is" vs "=="

a = [1, 2, 3]
b = a

print(a is b)
# True
print(a == b)
# True

c = list(a)

print(a == c)
# True
print(a is c)
# False

# • "is" expressions evaluate to True if two
#   variables point to the same object

# • "==" evaluates to True if the objects
#   referred to by the variables are equal

# Why Python Is Great:
# In-place value swapping

# Let's say we want to swap
# the values of a and b...
a = 23
b = 42

# The "classic" way to do it
# with a temporary variable:
tmp = a
a = b
b = tmp

# Python also lets us
# use this short-hand:
a, b = b, a


'''Why Python is Great: Namedtuples'''
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtuple('Car', 'color', 'mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print(my_car.color)

print(my_car.mileage)

# We get a nice string repr for free:
print(my_car)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'


'''Pretty Print Alternative'''
# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_mapping)  # {'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))
'''
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
'''

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: 'yup'})  # TypeError: keys must be a string


'''Get() method on dicts'''
# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(382))

print(greeting(333333))


'''How to merge two dictionaries'''
# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8


'''Different ways to test multiple flags at once in Python'''
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')


'''Sort a dictionary by value'''
# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))

# Or:

import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))


'''Function argument unpacking'''
def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

print(myfunc(*tuple_vec))
# 1, 0, 1

print(myfunc(**dict_vec))
# 1, 0, 1

