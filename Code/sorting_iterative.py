#!python

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items) - 1):

        if(items[i] > items[i+1]):
            return False

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if(len(items) < 2):
        return

    is_bad = True
    good_spots = 1
    while is_bad:

        swaps = 0
        for i in range(len(items) - good_spots):

            if(items[i] > items[i+1]):
                items[i], items[i+1] = items[i+1], items[i]
                swaps += 1

        is_bad = swaps > 0
        good_spots += 1


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if(len(items) < 2 or is_sorted(items)):
        return

    for i in range(len(items) - 1):
        min = i
        for j in range(i, len(items)):

            if(items[j] < items[min]):
                min = j

        items[min], items[i] = items[i], items[min]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if(len(items) < 2 or is_sorted(items)):
        return

    for i in range(1, len(items)):

        for j in range(0,i):

            if(items[i - j] < items[i-j-1]):
                items[i-j], items[i-j-1] = items[i-j-1], items[i-j]
            else:
                break


#print(bubble_sort([1,5,3,6,8]))
