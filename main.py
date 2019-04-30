import math
from datetime import date, timedelta
from scipy import special
from sys import maxsize
import itertools

def sphere_volume(r):
    """ a function that computes the volume of a sphere, given its radius r. """
    return 4/3*math.pi*r**3


def quadratic_equation(a, b, c):
    """ a function that computes the real roots of a given quadratic equation a*X^2+b*X+c=0. """
    d = math.sqrt(b**2-4*a*c)

    r1 = (-b+d)/(2*a)
    r2 = (-b-d)/(2*a)

    return (r1, r2)


def number_of_zeros(lst):
    """  a function that returns the number of zeros in a given simple list of numbers lst. """
    return len(list(filter(lambda x: x == 0, lst)))


def draw_pascal(n):
    """ a function that takes an integer n as a parameter and prints the first n rows of the Pascal's triangle. """
    # Iterate through every line
    # and print entries in it
    for line in range(0, n):

        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            print(bc(line, i), " ", "")
        # '/n'
        print()


def euler():
    """ returns the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit."""


def days(date1, date2):
    """a function that takes two dates, date1 and date2, in some format, and returns the number of days from date1 to date2, inclusive."""

    # this will give you a list containing all of the dates
    numDays = [str(date1 + timedelta(days=x))
               for x in range((date2-date1).days + 1)]

    return "\n".join(numDays)


def remove_consecutive_dups(lst):
    """ return a copy of lst with consecutive duplicates of elements eliminated. For example, for lst = [a, a, a, a, b, c, c, a, a, d, e, e, e, e], the returned list is [a, b, c, a, d, e]. """
    return [v for i, v in enumerate(lst) if i == 0 or v != lst[i-1]]


def remove_dups(lst):
    """ return a copy of lst with duplicates of elements eliminated. For example, for lst = [a, a, a, a, b, c, c, a, a, d, e, e, e, e], the returned list is [a, b, c, d, e]. """
    s = sorted(lst)
    return [v for i, v in enumerate(s) if i == 0 or v != s[i-1]]


def replicate(lst, n):
    """ Replicate each of the elements of lst a given number of times. For example, for lst = [a, b, c] and n = 3, the returned list is [a, a, a, b, b, b, c, c, c]. """
    def rep_helper(val, n):
        i = 0
        v = ""
        while i < n:
            v = v + val
            i += 1
        return v
    list_of_lists = [list(rep_helper(a, n)) for a in lst]
    return [val for sublist in list_of_lists for val in sublist]


def split_list(lst, n):
    """ split lst into two parts with the first part having n elements, and return a list that contains these two parts. """
    return [ lst[:n+1], lst[n+2:] ]

def min_max_median(lst):
    """ a function that takes a simple list of numbers lst as a parameter and returns a list with the min, max, and the median of lst. """
    s = sorted(lst)
    n = len(s)
    return [ s[0], s[-1], s[n//2] if n % 2 == 1  else (s[n//2 - 1] + s[n//2]) / 2]


def bc(n, k):
    """ return the binomial coefficient "n choose k". Can you figure out a method that is less likely to cause an overflow than using the formula(n*(n-1)*...*(n-k+1))/(k*(k-1)*...*2)? """

    return special.binom(n, k)


def subsets(s, n):
    """ return the set of n-element subsets of s. """
    return list(itertools.combinations(s, n)) 

def max_subarray(arr):
    """ return a contiguous subarray within arr which has the largest sum. """
    max_so_far = -maxsize - 1
    max_ending_here = 0
    max_itr = 0
    min_itr = 0

    for i in range(0, len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            temp = i
        if (temp > max_itr):
            min_itr = max_itr
            max_itr = temp

        if max_ending_here < 0:
            max_ending_here = 0
    return arr[min_itr:max_itr + 1]
