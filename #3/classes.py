"""
1. Create a class called Rectangle that has attributes width and height. Add methods area and perimeter
that calculate the area and perimeter of the rectangle, respectively."
"""
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return "The area is " + str(self.height*self.width)

    def perimeter(self):
        return "The perimeter is " + str((self.height + self.width)*2)

my_rectangle = Rectangle(5,10)
#print(my_rectangle.area())
#print(my_rectangle.perimeter())


"""
2. Create a class called Circle that has attribute radius. 
Add methods area and circumference that calculate the area and circumference of the circle, respectively."
"""
import math
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 'The area is ' + str(round(math.pi*pow(self.radius, 2), 2))

    def circumference(self):
        return 'The circumference is ' + str(round(math.pi*self.radius*2, 2))

my_circle = Circle(10)
#print(my_circle.area())
#print(my_circle.circumference())

"""
3. Create a class called Car that has attributes make, model, and year. 
Add methods start and stop that simulate starting and stopping the car, respectively."
"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car started")

    def stop(self):
        print("The car stopped")

my_car  = Car('Skoda', 'Octavia', 2010)
#my_car.start()
#my_car.stop()

"""
4. Create a class called Dice that has attribute sides (the number of sides on the dice). 
Add a method roll that generates a random number between 1 and the number of sides on the dice."
"""
import  random
class Dice():
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        print("The number is " + str(random.randint(1,self.sides)))

my_dice = Dice(6)
#my_dice.roll()

"""
5. Create a class called Temperature that has attribute celsius (a temperature in degrees Celsius). 
Add methods to_fahrenheit and to_kelvin that convert the temperature to degrees Fahrenheit and Kelvin, respectively."
"""
class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        print(self.celsius,  'degree(s) Celsius will make', (self.celsius*9/5 + 32), 'degree(s) Fahrenheit')

    def to_kelvin(self):
        print(self.celsius,  'degree(s) Celsius will make', (self.celsius+273.15), 'degree(s) Kelvin')

my_temp = Temperature(1)
#my_temp.to_fahrenheit()
#my_temp.to_kelvin()

"""
6. Create a class called Book that has attributes title, author, and publication_year. 
Add a method get_age that calculates how many years ago the book was published."
"""
import datetime
class Book():
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        print(f'The book "{self.title}" by {self.author} was published '
              f'{ datetime.date.today().year - self.publication_year} years ago')

my_book = Book('The adventures of Tom Sawyer', 'Mark Twein', 1876)
#my_book.get_age()

"""
7. Create a class called Rectangle that has attributes width and height. 
Add methods __str__ and __repr__ that return a string representation of the rectangle object."
"""
class Rectangle2():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'This rectangle has a width of {self.width} cm and a height of {self.height} cm '

    def __repr__(self):
        return f'Rectangle2({self.height},{self.width}) '

my_rectangle2 = Rectangle2(5,10)
print(str(my_rectangle2))
print(repr(my_rectangle2))

