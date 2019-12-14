#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    if len(numbers) < 2:
        return

    min = numbers[0]
    max = numbers[0]
    # find min and max
    for num in numbers:
        if num < min:
            min = num
        elif num > max:
            max = num

    if min == max:
        return

    # create buckets and count all occurences
    counts = [0] * (max - min + 1)
    for num in numbers:
        counts[num - min] += 1

    # mutate original input
    current_count = 0
    for i in range(len(numbers)):

        numbers[i] = current_count + min
        counts[current_count] -= 1
        while current_count < len(counts) and counts[current_count] == 0:
            current_count += 1




def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    if len(numbers) < 2:
        return

    min = numbers[0]
    max = numbers[0]
    # find min and max
    for num in numbers:
        if num < min:
            min = num
        elif num > max:
            max = num

    if min == max:
        return

    # create buckets
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    range_per_bucket = (max - min) / num_buckets

    # loop over all values and add to appropriate buckets
    for i in range(len(numbers)):

        num = numbers[i]
        print(num)
        remainder = num - min
        index = int((remainder / range_per_bucket) - 0.0001) # small offset to handle max value
        print(index)
        buckets[index].append(num)

    #sort each bucket
    for bucket in buckets:
        counting_sort(bucket)

    # mutate original input
    curr_index = 0
    for bucket in buckets:
        for num in bucket:
            numbers[curr_index] = num
            curr_index += 1


if __name__ == '__main__':
    #items = [5,1,2,3,5,4,2,3,1,5,6,7,1,2,9,1,2,3,7,8]
    import random
    min = 0
    max = 100
    count = 100
    items = [random.randint(min, max) for _ in range(count)]
    bucket_sort(items)
    print(items)
