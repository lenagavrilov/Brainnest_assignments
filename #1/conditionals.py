"""
Write a program that prompts the user for a string and checks whether the string is
a palindrome (i.e., the string reads the same forward and backward).
"""

def isPalindrom(user_str):
    backward_str = user_str[::-1]
    if user_str == backward_str:
        return True
    else:
        return False

"""
Write a program that takes in a list of integers and returns the sum of all even
numbers in the list.
"""
def sumOfEven(list_numbers):
    sum = 0
    for num in list_numbers:
        if num % 2 == 0:
            sum += num
    return sum
"""
Write a program that prompts the user for their age and checks whether they are
old enough to vote (i.e., 18 years old or older).
"""
def IsEligibleToVote():

    age = int(input('How old are you? '))

    if age >= 18 and age > 0:
            print("Eligible to vote")
    else:
            print("Not eligible for vote yet")

"""
Write a program that takes in a list of integers and returns the largest number in the
list that is also divisible by 3.
"""
def largestDivisibleByThree(list_numbers):
    divisibleByThree = [];
    for num in list_numbers:
        if num%3 == 0:
            divisibleByThree.append(num)

    return(max(divisibleByThree))

"""
Write a program that prompts the user for a number and checks whether the
number is a prime number (i.e., only divisible by 1 and itself).
"""

def isPrime(number):
    prime = False

    if number > 1:
        for i in range (2, int(number/2)+1):
            if number % i == 0:
               prime = False
               break
        else:
            prime = True
    else:
        prime = False

    if prime:
        print(f'Number {number} is a prime number.')
    else:
        print(f'Number {number} is not a prime number.')



if __name__ == "__main__":
   print('IsPalindrom returns: ' + str(isPalindrom('ababa')))
   #print('Sum of even numbers in the list is: ' + str(sumOfEven([1,6,3,5,10])))
   #IsEligibleToVote()
   #print('largest Number Divisible By Three: ' + str(largestDivisibleByThree([1,3,26,79,99,6,15,16])))
   #isPrime(18)

