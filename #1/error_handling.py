"""
Write a function that takes a list of integers as an argument, and returns the sum of
the integers. Use a try-except block to catch any ValueError exceptions that may be
raised when attempting to convert a string to an integer.
"""

def integersSum(my_list):
    sum = 0
    try:
        for item in myList:
            sum += int(item)
        return sum
    except ValueError:
        print('Look like not all the values are integers')
        return 0
    except TypeError:
        print('Look like not all the values are integers')
        return 0
    except:
        print('Something went wrong')
        return 0

"""
Write a function that takes a filename as an argument, and attempts to open the file.
Use a try-except block to catch any FileNotFoundError exceptions that may be
raised when attempting to open the file. If the file is successfully opened, the
function should return the contents of the file.
"""

def openMyFile(my_file):
    try:
        file = open(my_file, "r")
        print(file.read())
    except FileNotFoundError:
        print("File doesn't exists")
        return
    except PermissionError:
        print("Looks like you don't have permissions to open the file")
        return
    except IsADirectoryError:
        print("You are trying to open directory and not a single file")
        return
    except:
        print("Failed to open the file")
        return

"""
Write a function that takes a list of strings as an argument, and returns a new list
containing only the strings that can be successfully converted to a float. Use a tryexcept
block to catch any ValueError exceptions that may be raised when
attempting to convert a string to a float.
"""
def funcStringToFloat(my_list):
    new_list = []

    for item in my_list:
        try:
            new_list.append(float(item))
        except ValueError:
            print("Cannot convert item \'" + item + '\' to float')
            continue

    print (new_list)


"""
Write a function that takes a list of dictionaries as an argument, and returns the
value of a specified key from each dictionary. Use a try-except block to catch any
KeyError exceptions that may be raised when attempting to access a key that does
not exist in a dictionary.
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


def listOfDict(my_list, key1, key2):
    try:
        value1 = '\u0332'.join(my_list[0][key1])
        value2 = '\u0332'.join(my_list[1][key2])
        return ('The value for ' + key1 + ' is ' + value1 +
                ' and the value for ' + key2 + ' is ' + value2)
    except KeyError:
        return 'Looks like you are passing the key which doesn\'t exists'

"""
Write a function that takes a list of integers as an argument, and returns the largest
integer in the list. Use a try-except block to catch any ValueError exceptions that
may be raised when attempting to compare elements that are not integers.
"""

def maxOfInt(my_list):
    try:
        return max(my_list)
    except TypeError:
        return 'Looks like not all the items in the list are numbers'
    except ValueError:
        return 'Looks like not all the ites in the list are numbers'
    except:
        return 'Cannot parse the list'

if __name__ == '__main__':
   # print(integersSum([1,'h',5,7]))
   # openMyFile('test.txt')
   #funcStringToFloat(['1', 'f', 'c', '5.26'])
   #print(listOfDict(my_list_of_dicts, 'rain', 'sale'))
   print(maxOfInt([3,10,15,'1.25',20]))