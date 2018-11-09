# Author: Greg Goodrum
# Course: BIOL 6750 with Dr. Will Pearse
# Section: 10 - Optimization
# Exercise 10
# ----------------


# Example Equation: y = x**3 + 2x -3
# x=1 results in y = 0


# ---- Bisection ----


# Pick interval (min,max) over which to find a minimum
# Pick tolerance
# while (f(midpoint) - f(min) > t ) or (f(midpoint) > t):
#     Evaluate function at mid-point of interval (a,b)
#     Set min and max to (min,midpoint) or (midpoint,max) such that the interval contains 0


# Define the function to be tested
def f(x):
    return x**3 + 2*x - 3


def Bisection(interval_min, interval_max, tol):
    # Exit function if range was given incorrectly.
    if interval_min > interval_max:
        return("Interval min must be smaller than Interval max")
    # If the multiple of f(range limits) is greater than zero, then y does not equal zero within the range.
    elif f(interval_min)*f(interval_max) > 0:
        return("Cannot solve equation, does not cross 0 in range")
    else:
        # While the midpoint of the range does not result in a f(x) within the tolerance range.
        while (interval_max - interval_min)/2.0 > tol:
            # Calculate the midpoint of the range.
            interval_mid = (interval_min + interval_max)/2.0
            # If the new midpoint returns f(x) = 0, this the answer so it should be returned.
            if f(interval_mid) == 0:
                return interval_mid
            # If the range min and range mid result in a value less than 0, then f(x) results
            # in zero between them, and the range mid should become the new range max.
            elif f(interval_min)*f(interval_mid) < 0:
                interval_max = interval_mid
            # If neither above condition is true, then f(x)=0 somewhere between the midpoint
            # and the range max, so the range mid should become the new range min.
            else:
                interval_min = interval_mid
        # Once f(x) is within the range, return x as the solution
        return interval_mid


Bisection(-50,50,.0001)


# ---- Newton-Raphson ----


# Define the function to be tested
def f(x):
    return x**2


def NewtonRaphson(x, tol):
    # While f(x) is greater than the tolerance value, run the following loop
    while f(x) > tol:

        if f(x) == 0:
            return x
        else:
            # line formula : y = mx + b, where slope = m
            # Create two points by adding/subtracting tine (.0001) amount from x
            x_less = x - 0.0001
            x_more = x + 0.0001
            # Calculate slope between two points
            slope = (f(x_more) - f(x_less)) / (x_more - x_less)
            # Determine b value in y=mx+b line formula by setting y=0
            b = f(x) - (slope * 0)
            # Determine x value where tangent line y=0
            tan_x_intercept = (-1.0 * b)/slope
            # Replace original x with new tangent-x-intercept
            x = tan_x_intercept
            # Print included as a check for how the loop is functioning
            # print(x)
    print('Finished, the solution is ' + str(x))
    return(x)


NewtonRaphson(15, 0.001)


# ---- Author reference material ----

# Utilized material from source:
# https://steemit.com/mathematics/@dkmathstats/the-bisection-method-with-python-code
def Bisection(a, b, tol):
    if a > b:
        return("first value must be interval min, second value must be interval max")
    if f(a)*f(b) > 0:
        return("No root found, cannot solve within range")
    else:
        while (b-a)/2.0 > tol:
            midpoint = (a+b)/2.0
            if f(midpoint) == 0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return(midpoint)


Bisection(-7,50,.0001)
