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

def cocktail_sort(items):
    if(len(items) < 2):
        return

    end_stop = len(items)
    start_stop = 0
    is_REAL_bad = True
    step = 1
    backwards_modifier = 0

    while is_REAL_bad:
        print(items)
        swaps = 0
        for i in range(start_stop - backwards_modifier, end_stop - 1, step):
            if(items[i] > items[i + 1]):
                items[i], items[i + 1] = items[i + 1], items[i]
                swaps += 1

        is_REAL_bad = swaps > 0
        if(step == 1):
            end_stop -= 1
            backwards_modifier = 1
        else:
            start_stop += 1
            backwards_modifier = 0
        step *= -1
        start_stop, end_stop = end_stop, start_stop

def cocktail_sort_with_helpers(items):
    if(len(items) < 2):
        return

    last_unsorted = len(items)
    first_unsorted = 0
    current_helper = 0

    helper_functions = [_swap_up, _swap_down]
    swaps = 1
    while swaps > 0:

        print(items)
        swaps = helper_functions[current_helper](items,first_unsorted, last_unsorted)
        if(current_helper == 0):
            current_helper = 1
            last_unsorted -= 1
        else:
            current_helper = 0
            first_unsorted += 1

def _swap_down(items, stop, start):
    print("running down")
    swaps = 0
    for i in range(start, stop, -1):
        print(i)
        if(items[i] < items[i - 1]):
            items[i], items[i - 1] = items[i - 1], items[i]
            swaps += 1

    return swaps

def _swap_up(items, start, stop):
    print("running up")
    swaps = 0
    for i in range(start, stop - 1, 1):
        print(i)
        if(items[i] > items[i + 1]):
            items[i], items[i + 1] = items[i + 1], items[i]
            swaps += 1

    return swaps

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if(len(items) < 2 or is_sorted(items)):
        return

    for i in range(len(items) - 1):
        min = i
        for j in range(i + 1, len(items)):

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
if __name__ == '__main__':
    items = [5,1,2,77,9,3,4,6,8,11,15,10,0]
    cocktail_sort_with_helpers(items)
    print(items)
