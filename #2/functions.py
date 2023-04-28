"""
1. Write a program that takes a list of numbers and returns the largest number in the list."
"""


def largest_num(list_of_num):
    return 'The largest num is ' + str(max(list_of_num))


"""
2. Write a program that takes a string and returns the number of vowels in the string."
"""


def vowels_num(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for character in my_string.lower():
        if character in vowels:
            counter += 1

    # list_compr = len([character  for character in my_string.lower() if character in vowels])

    return (f'There are {counter} vowels in the string {my_string} ')


"""
3. Write a program that takes a list of strings and returns a new list that contains only the strings 
that start with the letter 'a'."
"""


def give_me_a(list_of_strings):
    return [item for item in list_of_strings if item.startswith('a')]


"""
4. Write a program that takes a sentence (string) and returns a dictionary with the count of each word in the sentence."
"""


def count_into_dict(my_string):
    count_words = {}
    words = my_string.split()
    for word in words:
        if word not in count_words.keys():
            count_words[word] = 1
        else:
            count_words[word] += 1
    return count_words


"""
5. Write a program that takes two lists of numbers and returns a new list that 
contains only the numbers that are common to both lists."
"""


def common_nums(list1, list2):
    return [item for item in list1 if item in list2]


"""
6. Write a program that takes a list of integers and returns a new list 
that contains only the prime numbers from the original list."
"""

def prime_time(list_of_int):
    prime_list = []
    for num in list_of_int:
        if num > 1:
            isPrime = True
            for i in range(2, num - 1):
                if num % i == 0:
                    isPrime = False
                    break
            if isPrime:
                prime_list.append(num)
    return prime_list

"""
7. Write a program that takes a string and returns the number of words in the string."
"""
def words_count(myString):
    return len([word for word in myString.split()])

"""
8. Write a program that takes a list of strings and returns a new list that contains 
only the strings that are palindrome."
"""

def find_palindrome(list_of_str):
    palindrom_str = []
    for item in list_of_str:
        reversed_item = item[::-1]
        if item == reversed_item:
            palindrom_str.append(item)
    return palindrom_str

"""
9. Write a program that takes a sentence (string) and returns a tuple of the most frequent word and its frequency.
"""
def freq(my_string):
    count_freq = {}
    for word in my_string.split():
        if word in count_freq.keys():
            count_freq[word] += 1
        else:
            count_freq[word] = 1
    return count_freq

if __name__ == '__main__':
    # print(largest_num([3,10,17,15]))
    # print(vowels_num('Orange'))
    # print(give_me_a(['banana', 'apple', 'Ananas', 'aqua']))
    # print(count_into_dict('I like going to the desert and make some pittas. I enjoy the desert'))
    # print(common_nums([1,3,5,6,10], [5,3,2,1,10,12]))
    # print(prime_time([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    # print(words_count("Write a program that takes a string"))
    # print(find_palindrome(["madam", "level", "civic","man","purpose","ababa"]))
    print(freq("this is a test sentence to test the test"))
