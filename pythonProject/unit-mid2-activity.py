# Function: 1. Get the number of a specific item. 2. Printing all the items until the specific item.
# Author: Eric Gao
# Date: Apr 10th, 2024


def play():
    stuff = ["Banana", "Apple", "Orange", "Pineapple", "JF Kennedy", "AP CSA", "JF Kennedy"]
    item = "JF Kennedy"

    print(f"Number of {item} is {numItem(stuff, item)}")

    print()

    print(f"Printing all the items until {item}:")
    untilItem(stuff, item)


def numItem(list, item: str):
    item = item.strip().lower()
    counter = 0
    for i in list:
        i = i.strip().lower()
        if i == item:
            counter += 1
    return counter


def untilItem(list, item:str):
    item = item.strip().lower()
    for i in list:
        print(i)
        i = i.strip().lower()
        if i == item:
            break

play()