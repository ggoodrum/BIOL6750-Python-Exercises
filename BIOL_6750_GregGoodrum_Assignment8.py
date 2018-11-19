# Author: Greg Goodrum
# Course: BIOL 6750 with Dr. Will Pearse
# Section: 8 - Introduction to Python
# Exercise 8
# ----------------


# ---- Question 1 ----
# 1(a) Write a loop that prints out the numbers from 20 to 10
# range(start value, end value, step interval)
for i in (range(20, 9, -1)):
    print(i)
print("End; 1(a)")

# 1(b) Write a list comprehension that returns the numbers from 20 to 10
# [operation to perform(iteration to perform on) for definition of values]
descending_comprehension = [print(each) for each in range(20,9,-1)]
print("End: 1(b)")


# ---- Question 2 -----
# 2(a) Write a loop that prints out only the numbers from 20 to 10 that are even
for i in (range(20,9,-2)):
    print(i)
print("End: 2(a)")

# alternative version using remainder and conditional statement
for i in range(20,9,-1):
    if i%2 == 0:
        print(i)
print("End: 2(a)")

# 2(b) Write a list comprehension that prints out only the numbers from 20 to 10 that are even
even_descending_comprehension = [print(each) for each in range(20,9,-2)]
print("End: 2(b)")

# alternative version using remainder and conditional statement
even_descending_comprehension_remainder = [print(each) for each in range(20,9,-1) if each%2 == 0]
print("End: 2(b)")


# ---- Question 3 ----
# 3 Write a function that calculates whether a number is a prime number
def check_prime(x):
    if x%2 == 0:
        print(str(x) + " is not prime.")
    else:
        print(str(x) + " is prime.")


check_prime(10)
check_prime(13)
print("End: 3")


# ---- Question 4 ----
# 4 Write a function that calculates population size at any time for any values of it's parameters
# Gompertz curve: y(t) = a.e^(-b.e^(-c.t))
# y = population size, t = time, a, b, and c = parameters, e = exponential function

def gompertz_funct(time,parameter_a,parameter_b,parameter_c):
    import math
    popul_size_time = parameter_a * math.exp((-1.0 * parameter_b) * math.exp((-1.0 * parameter_c) * time))
    print(popul_size_time)


gompertz_funct(10.0, 5.0, 3.0, 7.0)
print("End: 4")


# ---- Question 5 ----
# 5(a) Implement a point class that holds x and y information for a point in space.

class Point:
    def __init__(self, xcoor, ycoor):
        self.xcoor, self.ycoor = xcoor, ycoor

    def pointtest(self):
        return "Point has an xcoor of " + str(self.xcoor) + " and a ycoor of " + str(self.ycoor)


Pt1 = Point(5,7)
Pt2 = Point(3,3)
print(Pt1.pointtest())
print(Pt2.pointtest())
print("End: 5(a)")

# 5(b) Write a distance method that calculates the distance between two points in space

class Point:
    def __init__(self, xcoor, ycoor):
        self.xcoor, self.ycoor = xcoor, ycoor

    def pointtest(self):
        print("Point has an xcoor of " + str(self.xcoor) + " and a ycoor of " + str(self.ycoor))

    def pointdist(self, pnt2):
        import math
        ydist = pnt2.ycoor - self.ycoor
        xdist = pnt2.xcoor - self.xcoor
        distance = math.sqrt((ydist**2) + (xdist**2))
        print("The distance between the points is " + str(distance) + " units.")


Pt1 = Point(5,7)
Pt2 = Point(3,3)
print(Pt1.pointdist(Pt2))
print("End: 5(b)")


# 5(c) Implement a line class that takes two point objects and makes a line between them.

class Line:
    def __init__(self, point1, point2):
        self.xstart, self.xend, self.ystart, self.yend = point1.xcoor, point2.xcoor, point1.ycoor, point2.ycoor


def distance_line(self):
    import math
    ydist = self.yend - self.ystart
    xdist = self.xend - self.xstart
    distance = math.sqrt((ydist**2) + (xdist**2))
    return "The distance between the points is " + str(distance) + " units."


Line1 = Line(Pt1, Pt2)
print(distance_line(Line1))
print("End: 5(c)")


# ---- Question 6 ----
# 6. Write a function that loads a text file, loops over the lines in it, and prints out the fifth
# character on the fifth line of that file.
# Hint:
# with open("name_of_file") as handle:
#       for line in handle:
#           Do Something
# Note: .txt and .rft files are interpreted differently in python, .txt behaves more reasonably

# Script that prints out the fifth line in the text file
#def fifthchar_fifthline(filepath):
    #with open(filepath) as txtfile:
        #for line in txtfile:
            #print(line)

# Prints 5th letter for every line
#def fifthchar_fifthline(filepath):
    #with open(filepath) as txtfile:
        #for line in txtfile:
            #print(line[4:5])

# Prints 5th letter for the 5th line
def fifthchar_fifthline(filepath):
    with open(filepath) as txtfile:
        for i, line in enumerate(txtfile):
            if i == 4:
                print(line[4:5])


# Test code for checking success of function
# I have included a copy of the text file used for this example in my GitHub repository as 'TextFile_for_Assignment8_Q5'
#fifthchar_fifthline("/Users/gregorygoodrum/USU/Coursework/Programming for Biologist (BIOL 6750)/Extra/TextFile_for_Python1.txt")

print("End: 6")
print('---- END: Exercise 8 ----')