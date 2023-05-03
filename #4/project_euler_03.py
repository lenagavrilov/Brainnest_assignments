"""
1. In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import math


def two_pound_quest():
    ways_possible = [0] * 201
    ways_possible[0] = 1
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(coin, 201):
            ways_possible[i] += ways_possible[i - coin]

    print( ways_possible[200])

"""
2. We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.
    The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.
    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def pandigital_products_sum():
    product = set()
    proper_set = set('123456789')
    for i in range(0, 99):
        for j in range(0, 9999):
            pan = str(i) + str(j) + str(i*j)
            if len(pan) == 9 and set(pan) == proper_set:
                product.add(i*j)
            elif len(pan) >9:
                break
    print(sum(product))


"""
3.  The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it 
    may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, 
    less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from fractions import Fraction
def find_denominator():
    product_result = 1
    for numerator in range(10,100):
        for denominator in range(numerator+1, 100):
            num_common = list(set(str(numerator))&set(str(denominator)))
            if len(num_common) != 0:
                if num_common[0] != '0':
                    num = list(str(numerator))
                    denum = list(str(denominator))
                    num.remove(num_common[0])
                    denum.remove(num_common[0])
                    if num[0] != '0' and denum[0] != '0':
                        if Fraction(int(num[0]), int(denum[0])) == Fraction(numerator,denominator):
                            product_result *= Fraction(numerator,denominator)

    print(product_result.denominator)

from math import factorial
"""
4. 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
   Find the sum of all numbers which are equal to the sum of the factorial of their digits.
   Note: As 1! = 1 and 2! = 2 are not sums they are not included.   
"""

def find_sum_factorials(num):
    sum_fact = 0
    for i in str(num):
        sum_fact += factorials[int(i)]
    return sum_fact


def equal_factorial():
    global factorials
    factorials = [1]
    for i in range(1,10):
        factorials.append(math.factorial(i))

    total_sum = 0
    for num in range(3, 9999999):
        if num == find_sum_factorials(num):
            total_sum += num
   
    print(total_sum)


"""
5.The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
  There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
  How many circular primes are there below one million?
"""

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False

    return True


def create_rotations_lists(num_list):
    rotation_list = []
    for i in num_list:
        num_list = num_list[1:] + num_list[:1]
        number_to_add  = ''.join(str(x) for x in (num_list))
        rotation_list.append(number_to_add)
    return rotation_list


def circular_primes():
    counter = 1 #include number 2 which is only prime even num
    for num in range (1, 1000000,2):
        if set('246850')&set(str(num)) and len(str(num)) >1:
            continue #Any number containing these digits won't be prime at least in one rotation, not included one-digits
        all_primes = True
        rotations_list = []
        num_list = [int(x) for x in str(num)]
        rotations_list = create_rotations_lists(num_list)

        for i in rotations_list:
            if not is_prime(int(i)):
                all_primes = False
                break
        if not all_primes:
            continue
        else:
            counter +=1
    print(counter)


if __name__ == '__main__':
    #two_pound_quest()
    #pandigital_products_sum()
    # find_denominator()
    # equal_factorial()
    circular_primes()
