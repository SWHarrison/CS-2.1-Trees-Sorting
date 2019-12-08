class B_plus_tree_node:

    def __init__(self, is_leaf = True):

        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next_leaf = None

    def add_node(self, key, new_node):

        for i in range(len(self.keys)):
            if key < self.keys[i]:
                #self.children[i] = new_node # change to insert at i
                self.children = self.children[0:i] + [key] + self.children[i:]
                return

        self.children.append(new_node)

    def __repr__(self):
        return str(self.keys)

class B_plus_tree:

    def __init__(self,order = 4):

        self.root = None
        self.size = 0
        self.order = order

    def is_empty(self):
        return self.size == 0

    def insert(self,item):

        # empty tree creates root
        if self.is_empty():
            self.root = B_plus_tree_node()
            self.root.keys.append(item)
            self.size += 1
        else:
            current_node = self.root
            eject = self._insert_helper(current_node, item)
            if eject != None:
                self.root = B_plus_tree_node(False)
                self.root.keys.append(eject[0])
                self.root.children.append(eject[2])
                self.root.children.append(eject[1])

    ''' From Wikipedia B+ tree article
    Perform a search to determine what bucket the new record should go into.
    If the bucket is not full (at most b − 1) entries after the insertion), add the record.
    Otherwise, before inserting the new record
    split the bucket
    original node has ⎡(L+1)/2⎤ items
    new node has ⎣(L+1)/2⎦ items
    Move ⎡(L+1)/2⎤-th key to the parent, and insert the new node to the parent.
    Repeat until a parent is found that need not split.
    If the root splits, treat it as if it has an empty parent and split as outline above.'''
    def _insert_helper(self, current_node, item):
        """
        Recursive helper function that adds new item to tree.
        Always adds item to leaf node, then pushes middle value up if needed.
        """

        if current_node.is_leaf:

            print("current node is:",current_node)
            current_node.keys.append(item)
            keys = current_node.keys
            index = len(keys) - 1
            while index > 0 and keys[index] < keys[index - 1]:
                print(item, "is smaller than",keys[index - 1])
                print("swapping")
                keys[index], keys[index - 1] = keys[index - 1], keys[index]
                print(current_node)
                index -= 1
            # if number of keys is greater than maximum number of keys, eject middle key to parent
            if len(keys) >= self.order:
                print("current node full, ejecting")
                print("current node before ejection:",current_node)
                mid = len(keys) // 2
                #eject = keys.pop(len(keys)//2)
                eject = keys[mid]
                new_node = B_plus_tree_node()
                new_node.keys = keys[mid:]
                new_node.next_leaf = current_node.next_leaf
                current_node.keys = keys[0:mid]
                current_node.next_leaf = new_node
                return (eject, new_node, current_node)
            else:
                return None

        else:
            child_index = len(current_node.keys)
            for i in range(len(current_node.keys)):
                print("item:",item,"key:",current_node.keys[i])
                if item < current_node.keys[i]:
                    print(item," is less than",current_node.keys[i])
                    child_index = i
                    break
            print("child index is",child_index, "node will be",current_node.children[child_index])
            child_node = current_node.children[child_index]
            ejected_item = self._insert_helper(child_node, item)

            if ejected_item == None:
                return None
            else:
                to_add = ejected_item[0]
                new_node = ejected_item[1]
                old_node = ejected_item[2]
                current_node.add_node(to_add, new_node)
                # should now handle next_leaf when at leaf level
                #if old_node.is_leaf:
                #   old.node.next_leaf = new_node

                current_node.keys.append(to_add)
                keys = current_node.keys
                index = len(keys) - 1
                while index > 0 and keys[index] < keys[index - 1]:
                    keys[index], keys[index - 1] = keys[index - 1], keys[index]
                # if number of keys is greater than maximum number of keys, eject middle key to parent
                if len(keys) >= self.order:
                    mid = len(keys) // 2
                    #eject = keys.pop(len(keys)//2)
                    eject = keys[mid]
                    new_node = B_plus_tree_node()
                    new_node.keys = keys[0:mid]
                    current_node.keys = keys[mid + 1:]
                    return (eject, new_node, current_node)
                else:
                    return None

def test_bptree():

    tree = B_plus_tree()
    items = [40,30,20,50,60,10,70]
    for item in items:
        print("inserting", item)
        tree.insert(item)
        print("root",tree.root)
        print("children",len(tree.root.children))
        for child in tree.root.children:
            print(child)

if __name__ == '__main__':
    test_bptree()
