#!python

from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.
    Item pairs are stored in a binary min heap for its efficient operations."""

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize new binary min heap to store items in this priority queue
        self.heap = BinaryMinHeap()
        self.curr_id = 0

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.size(), self.front())

    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """Insert the given item into this priority queue in order according to
        the given priority."""
        # Insert given item into heap in order according to given priority
        new_entry = (priority, self.curr_id, item)
        self.heap.insert(new_entry)
        self.curr_id += 1

    def front(self):
        """Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty."""
        if self.length() == 0:
            return None
        return self.heap.get_min()[2]

    def dequeue(self):
        """Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty."""
        if self.length() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # Remove and return minimum item from heap
        return self.heap.delete_min()[2]

    def push_pop(self, item, priority):
        """Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority.
        This method is more efficient than calling dequeue and then enqueue."""
        if self.length() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        to_return = self.front()
        self.heap.items[0] = (priority, self.curr_id, item)
        self.heap._bubble_down(0)
        return to_return

def test_priority_queue():

    pri_q = PriorityQueue()
    items = ["Sam","Suk","Zurich","Tom","Alan","Betsy","Eirika","Kevin","Ali"]
    priority = 0
    for item in items:
        print("adding",item,"with priority",priority)
        pri_q.enqueue(item, priority)
        priority = (priority + 1)%3

    while pri_q.length() > 0:
        print(pri_q.dequeue())

    items = ["Sam","Suk","Zurich","Tom","Alan","Betsy","Eirika","Kevin","Ali"]
    priority = 0
    for item in items:
        print("adding",item,"with priority",priority)
        pri_q.enqueue(item, priority)
        priority = (priority + 1)%3

    print(pri_q.push_pop("Jackson", 4))
    print(pri_q.heap.items)

    while pri_q.length() > 0:
        print(pri_q.dequeue())

if __name__ == '__main__':
    test_priority_queue()
    PQ = PriorityQueue()
    assert(PQ.is_empty())
    assert(PQ.length() == 0)
    PQ.enqueue("apple", 2)
    assert(PQ.length() == 1)
    assert(PQ.front() == "apple")
    assert(PQ.length() == 1)
    PQ.enqueue("orange", 0)
    assert(PQ.length() == 2)
    assert(PQ.front() == "orange")
    assert(PQ.length() == 2)
    assert(PQ.dequeue() == "orange")
    assert(PQ.length() == 1)
    assert(PQ.push_pop("banana", 4) == "apple")
    assert(PQ.length() == 1)
    assert(PQ.front() == "banana")
    assert(PQ.length() == 1)
