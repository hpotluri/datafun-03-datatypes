"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics

# TODO: import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
list1 = [10, 20, 13, 14, 24, 12, 14, 53, 22, 53, 65, 77, 87, 45, 87, 96, 75, 98, 78, 96, 85, 70, 30, 95, 90]

listx = [x for x in range(1, 11)]

listy = [5, 8, 10, 12, 16, 18, 20, 22, 24, 27]


# TODO: define some custom functions
def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numeric list."""
    logger.info("============list Statistics section=============")
    logger.info(f"List1: {list1}")

    # Descriptive: Averages and measures of central tendency
    # Use statistics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"stdev: {stdev}")
    logger.info(f"variance: {variance}")


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numeric list."""
    logger.info("============list correlation and prediction section=============")
    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statistics module to get correlation between list1 and list2

    correlationxy = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationxy}")

    # Predictive: Machine Learning - Linear Regression
    # If the correlation is close to 1.0, then the data is linearly related
    # If so, use statistics module to get linear regression for list1 and list2
    # This is a form of supervised machine learning - it uses all known data
    # Use the slope and intercept and an unknown (future) x to predict a y value
    # Python functions can return multiple values

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

    x_max = max(listx)
    newx = x_max * 15  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info(f"We predict that when x = {newx}, y will be about {newy}")


def illustrate_list_built_in_functions():
    logger.info("============list built-in functions section=============")
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calculate the max and min scores
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Given score list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    list1_set = set(list1)
    logger.info(f"Given list1 as set: {list1_set}")
    # Return a new list sorted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list sorted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )


def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """
    logger.info("============list methods section=============")
    # append an item to the end of the list
    lst = [15, 12, 43]
    lst.append(49)

    # extend the list with another list
    lst.extend([49, 51, 63])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 42
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 42
    lst.remove(item_to_remove)

    # Count how many times 111 appears in the list
    ct_of_111 = list1.count(70)

    # Sort the list in ascending order using the sort() method
    asc_scores2 = list1.sort()

    # Sort the list in descending order using the sort() method
    desc_scores2 = list1.sort(reverse=True)

    # Copy the list to a new list
    new_scores = list1.copy()
    logger.info(f"new_scores is: {new_scores}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_scores.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_scores}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_scores.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_scores is: {new_scores}"
    )


def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""
    logger.info("============list transformations section=============")
    logger.info(f"list1: {list1}")

    # TRANSFORMATIONS ............................

    # FILTER and MAP are critical transformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include scores greater than 100
    # You could pass in a named function, but honestly this is easier
    # Say "KEEP x such that x > 100 is True" given list1
    # Cast the result using square brackets to get back a list
    scores_below_80 = [x for x in filter(lambda x: x < 80, list1)]
    logger.info(f"Scores below 80: {scores_below_80}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    # Say "map x to x cube root of x" given list1
    # Cast the result using square brackets to get a list
    cbrt_scores = [x for x in map(lambda x: math.cbrt(x), list1)]

    logger.info(f"Cube-root scores: {cbrt_scores}")

    # Map each element to calculate the volume of a cube with a side equal to the value in your list
    # Say "map x to the square root of x" given score_list
    # remember to cast the result to a list (using square brackets)
    cube_scores = [x for x in map(lambda x: x * x * x, list1)]
    logger.info(f"Volume of cubes: {cube_scores}")


def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""
    logger.info("============list comprehensions section=============")
    logger.info(f"list1: {list1}")

    # TRANSFORMATIONS - Using List Comprehensions
    # List Comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise
    # They are the preferred "pythonic" way to do transformations
    # They are faster than map / filter - it's quite impressive when you master them!

    # With comprehensions, we start with what we WANT
    # Filter the new list to only include scores greater than 80
    # Say "KEEP x (for each x in score_list) IF  x > 80"
    # Cast the result to a list using square brackets

    scores_over_80 = [x for x in list1 if x > 80]
    logger.info(f"Scores over 80 (using list comprehensions!): {scores_over_80}")

    # Map each element to its triple value
    # Say "give me x tripled (for each x in score_list)"
    # Cast the result to a list using square brackets

    triple_scores = [x * 3 for x in list1]
    logger.info(f"Tripled scores (using list comprehensions!): {triple_scores}")

    # Map each element to calculate the volume of a cube with a side equal to the value in your list
    # Say "map x to the square root of x" given score_list
    # remember to cast the result to a list (using square brackets)
    cube_scores = [x * x * x for x in list1]
    logger.info(f"Volume of cubes: {cube_scores}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    # call your functions here (see instructions)
    print("Replace this with calls to your functions.")
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    show_log()
