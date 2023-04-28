"""
1. Create a for loop that iterates through a list of strings and prints each string in uppercase.
"""

def uppercase_string(list_of_strings):
    for item in list_of_strings:
        print(item.upper())


"""
2. Create a for loop that iterates through a list of numbers and prints the square of each number."
"""
def list_square(list_of_int):
    for num in list_of_int:
        print(num**2)

"""
"3. Create a for loop that iterates through a list of dictionaries and prints the value 
of a specified key for each dictionary."
"""
my_list_of_dicts =[
    {
        'sky': 'blue',
        'rain': 'Nope!'
    },
    {
        'shopping': True,
        'price_max': 100,
        'sale': 'YESS!'
    }
]

def listOfDict(my_list, *keys):
    for dict in my_list:
        for k, v in dict.items():
            print(str(k) + ': ' + str(v))

"""
4. Create a for loop that iterates through a list of numbers and prints the largest number in the list.
"""
def largest_num(list_of_int):
    largest = list_of_int[0]
    for i in list_of_int:
        if i > largest:
            largest = i
    print('The largest number is ' + str(largest))

"""
5. Create a for loop that iterates through a list of lists and prints the sum of the elements in each sub-list.
"""
def sublist_sum(my_list):
    for list_item in my_list:
        print(sum(list_item))


if __name__ == '__main__':
    #uppercase_string(['apple', 'banana', 'strawberry'])
    #list_square([3,4,5])
    #listOfDict(my_list_of_dicts)
    #largest_num([1, 7, 3, 5, 2])
    sublist_sum([[1,2,3],[3,3,3,3],[15,2]])


