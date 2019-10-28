#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    index_1 = 0
    index_2 = 0

    to_return = []

    while index_1 < len(items1) and index_2 < len(items2):

        if items1[index_1] < items2[index_2]:
            to_return.append(items1[index_1])
            index_1 += 1
        else:
            to_return.append(items2[index_2])
            index_2 += 1

    if(index_1 >= len(items1)):
        to_return += items2[index_2:]
    else:
        to_return += items1[index_1:]

    return to_return


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if(len(items) <= 1):
        return items

    mid = len(items)//2
    left_half = merge_sort(items[0:mid])
    right_half = merge_sort(items[mid:])

    return merge(left_half, right_half)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot = items[low]
    swap_index = low + 1

    for i in range(low+1, high):
        if items[i] < pivot:
            items[i], items[swap_index] = items[swap_index], items[i]
            swap_index += 1

    items[low], items[swap_index-1] = items[swap_index-1], items[low]
    return (swap_index - 1)


def quick_sort(items):

    _quick_sort(items, 0, len(items))


def _quick_sort(items, low, high):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    print(items[low:high])
    # Check if list or range is so small it's already sorted (base case)
    if (high - low) < 2:
        return
    # Partition items in-place around a pivot and get index of pivot
    swap_point = partition(items, low, high)
    # TODO: Sort each sublist range by recursively calling quick sort
    _quick_sort(items,low, swap_point)
    _quick_sort(items,swap_point + 1, high)


if __name__ == '__main__':
    items1 = [2,4,5,8,10,13,14]
    items2 = [1,3,6,7,9,11,12]
    items = ['Z','a','b','e','E','F']
    itemNumbers = [1,78,12,45,13,84,11,8,56,14,54,42,89,35,25,66,76]
    #print(merge(items1, items2))
    #print(merge_sort(items))
    #print(merge_sort(itemNumbers))
    quick_sort(itemNumbers)
    print(itemNumbers)
