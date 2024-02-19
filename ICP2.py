# 1. Use a python code to display the following star pattern using the for loop
def star():
    for i in range(10):  # set number of lines in the pattern
        if i <= 5:  # first five lines set to i
            for x in range(i):
                print("*", end=" ")
            print()  # seperate lines
        else:
            for x in range(10 - i):  # last five lines set to 10-i
                print("*", end=" ")
            print()
    print()


# 2. Use looping to output the elements from a provided list present at odd indexes


def oddindices(my_list):
    for i in range(len(my_list)):  # repeat for each item in list
        if i % 2 != 0:  # determine odd indices
            print(my_list[i])
    print()


# 3. Write a code that appends the type of elements from a given list.


def listtype(my_list):
    new_list = []  # new list
    for i in range(len(my_list)):
        new_list.append(type(my_list[i]))  # new list appended the type of each element of a list
    print(my_list)
    print(new_list)
    print()


# 4. Write a function that takes a list and returns a new list with unique items of the first list


def uniquelist(my_list):
    new_list = []  # declare new list

    for i in range(len(my_list)):
        if my_list[i] not in new_list:  # determines if new_list has the indicated element
            new_list.append(my_list[i])

    print(new_list)
    print()


# 5. Write a function that accepts a string and calculate the number of upper-case letters and lower-case letters.

def countcases():
    lower = 0
    upper = 0

    print('Enter a String: ', end="")
    str = input()

    for i in str:
        if i.islower():  # determine if letter is lower case
            lower += 1
        else:
            if i != " ":  # ignore spaces
                upper += 1

    print("No. of Upper-case characters: ", upper)
    print("No. of Lower-case Characters: ", lower)


# main


list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_2 = [23, "Python", 23.98]
list_3 = [1, 2, 3, 3, 3, 3, 4, 5]

star()
oddindices(list_1)
listtype(list_2)
uniquelist(list_3)
countcases()
