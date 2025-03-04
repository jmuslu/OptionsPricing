"""
Joseph Muslu
DS2000: SEC 2
HW4
"""

import random
import time
import matplotlib.pyplot as plt


def make_dice_list(int_len, int_sides):
    # this function creates a list for rolls of a die

    # the parameters are the length of the list (amount of rolls)
    # and the number of sides of the dice

    # the return value is a list

    rolls_list = []
    for i in range(int_len):
        roll = random.randint(1, int_sides)
        rolls_list.append(roll)

    return rolls_list


def display_roll_info(int_list):
    # this function gives information about a list of rolls, in the
    # length of the list, the first 10 numbers, the max value, and the minimum value
    # and then prints them

    # the parameter is a list of integers

    # there is no return value

    length_of_list = len(int_list)

    first_10 = int_list[:10]

    max_val = max(int_list)
    min_val = min(int_list)

    print ("The length of this list is", length_of_list, "rolls long")
    print ("The first 10 numbers in this list are", first_10)
    print("The maximum value in this list is", max_val)
    print("The minimum value in this list is", min_val)


def my_count(list, int_value):
    # this function looks at the numbers in a list and determines how many times
    # a number repeats in this list

    # the parameters are a list, and an integer value

    # the return value is the count of how many times this number appeared in the list

    count = 0

    for i in range(len(list)):
        if list[i] == int_value:
            count = count + 1

    return count


def my_sum(list):
    # this function calculates the sum of all values in the list

    # the parameters are a list

    # the return value is the sum of all values in the list as an int

    sum = 0

    for i in range(len(list)):
        sum = sum + list[i]

    return sum


def my_min(ls):

    # this function finds the lowest value in the list

    # the parameters are the list

    # the return value is the lowest number in the list as an int
    minimum_value = ls[0]

    for i in range(len(ls)):
        if ls[i] < minimum_value:
            minimum_value = ls[i]

    return minimum_value


def visualize_sum_funcs(int_max, int_sides):
    # this function visualizes a graph that compares the built in sum function
    # to my sum function and its performance in time over different lengths of lists

    # the parameters are a maximum list size as an int, and an integer number of sides
    # for dice rolls

    # there is no return value


    period_increment = int_max // 20

    period_increments = []
    for i in range(20):
        period_increments.append((period_increment * (i + 1)))


    dice_lists = []
    for i in range(20):
        dice_list = make_dice_list(period_increments[i], int_sides)
        dice_lists.append(dice_list)


    times_my_sum = []
    for i in range(20):
        start_sum_time = time.time()
        my_sum(dice_lists[i])
        end_sum_time = time.time()
        time_elapsed_sum = end_sum_time - start_sum_time
        times_my_sum.append(time_elapsed_sum)


    times_sum = []
    for i in range(20):
        start_sum_time = time.time()
        sum(dice_lists[i])
        end_sum_time = time.time()
        time_elapsed_sum = end_sum_time - start_sum_time
        times_sum.append(time_elapsed_sum)


    plt.plot (period_increments, times_my_sum, label = "my_sum function", marker = "o",  color = "blue" )
    plt.plot(period_increments, times_sum, label = "sum function", marker = "o", color = "red" )
    plt.xlabel("Length of List")
    plt.ylabel("Time Elapsed to Sum List")
    plt.legend()
    plt.savefig("sum_vs_my_sum.png")
    plt.show()


def main():


    # this uses a function to roll a die of 10 sides 1000000 times and uses
    # another function to give information about the rolls and times it
    print("Test 1\n")
    start1 = time.time()
    list1 = make_dice_list(1000000,10)
    end1 = time.time()
    display_roll_info(list1)
    print("\n")

    # this does the same thing as the previous lines of code, but the
    # numbers used in the function input for the dice list are different
    print("Test 2\n")
    start2 = time.time()
    list2 = make_dice_list(1000, 10)
    end2 = time.time()
    display_roll_info(list2)
    print("\n")

    # this calculates the time elapsed by subtracting starting and ending time of the previous functions
    time_elapsed1 = round(end1 - start1, 7)
    time_elapsed2 = round(end2 - start2, 7)

    # outputs information to user
    print("The time elapsed in generating list 1 is", time_elapsed1, "seconds")
    print("The time elapsed in generating list 2 is", time_elapsed2, "seconds")

    print("\n")

    # this code calculates the amount of time passed for using the my count function
    # and compares the output values of original and my functions
    print("For 1000000 element list:")
    start3 = time.time()
    my_count_val = my_count(list1, 4)
    end3 = time.time()
    time_elapsed3 = round(end3 - start3, 7)

    print("The time elapsed in running my_count of 4 is", time_elapsed3, "seconds")

    count_val = list.count(list1,4)
    print("The result of my_count of 4 is",my_count_val)
    print("The result of list.count of 4 is", count_val)

    if my_count_val == count_val:
        print("These values are the same\n")

    elif my_count_val != count_val:
        print("These values are not the same\n")


    # this code calculates the amount of time passed for using the my sum function
    # and compares the output values of original and my functions
    print("For 1000000 element list:")
    start4 = time.time()
    my_sum_val = sum(list1)
    end4 = time.time()
    time_elapsed4 = round(end4 - start4, 7)

    print("The time elapsed in running my_sum is", time_elapsed4, "seconds")

    sum_val = sum(list1)
    print("The result of my_sum is",my_sum_val)
    print("The result of sum of 4 is", sum_val)

    if my_sum_val == sum_val:
        print("These values are the same\n")

    elif my_sum_val != sum_val:
        print("These values are not the same\n")


    # this code calculates the amount of time passed for using the my min function
    # and compares the output values of original and my functions
    print("For 1000000 element list:")
    start5 = time.time()
    my_min_val = min(list1)
    end5 = time.time()
    time_elapsed5 = round(end5 - start5, 7)

    print("The time elapsed in running my_min is", time_elapsed5, "seconds")

    min_val = min(list1)
    print("The result of my_min is",my_sum_val)
    print("The result of min is", sum_val)

    if my_min_val == min_val:
        print("These values are the same\n")

    elif my_min_val != min_val:
        print("These values are not the same\n")


    visualize_sum_funcs(1000000,6)


main()