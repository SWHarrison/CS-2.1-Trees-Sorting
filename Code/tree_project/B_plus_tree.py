class B_plus_tree_node:

    def __init__(self, is_leaf = True):

        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next_leaf = None

    # currently unused and non-functional
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

    def contains(self, item):

        if self.is_empty():
            return False

        current_node = self.root
        while current_node.is_leaf == False:
            print(current_node)
            child_index = 0
            while child_index < len(current_node.keys) and item >= current_node.keys[child_index]:
                print(item, " is greater than or equal to", current_node.keys[child_index])
                child_index += 1

            current_node = current_node.children[child_index]
        print("current node is",current_node, "checking for", item)
        print("current node leaf?", current_node.is_leaf)
        return item in current_node.keys

    def all_values(self):

        to_return = []
        current_node = self.root
        while current_node.is_leaf == False:
            current_node = current_node.children[0]

        while current_node.next_leaf:

            for item in current_node.keys:
                to_return.append(item)

            current_node = current_node.next_leaf

        for item in current_node.keys:
            to_return.append(item)

        return to_return

    def insert(self,item):

        # empty tree creates root
        if self.is_empty():
            self.root = B_plus_tree_node()
            self.root.keys.append(item)
            self.size += 1
        else:
            current_node = self.root
            eject = self._insert_helper(current_node, item)
            self.size += 1
            if eject != None:
                self.root = B_plus_tree_node(False)
                self.root.keys.append(eject[0])
                self.root.children.append(eject[2])
                self.root.children.append(eject[1])
                print("new root is",self.root)
                print("children are",self.root.children)

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
                print("ejecting",eject)
                new_node = B_plus_tree_node()
                new_node.keys = keys[mid:]
                new_node.next_leaf = current_node.next_leaf
                current_node.keys = keys[0:mid]
                current_node.next_leaf = new_node
                print("new node (right)",new_node)
                print("old node (left)",current_node)
                return (eject, new_node, current_node)
            else:
                return None

        else:
            child_index = len(current_node.keys)
            for i in range(len(current_node.keys)):
                print("item:",item,"key:",current_node.keys[i])
                if item <= current_node.keys[i]:
                    print(item," is less than",current_node.keys[i])
                    child_index = i
                    break
            print("child index is",child_index, "node will be",current_node.children[child_index])
            child_node = current_node.children[child_index]
            ejected_item = self._insert_helper(child_node, item)

            if ejected_item == None:
                return None
            else:
                print("ejected items",ejected_item)
                print("current_node",current_node)
                print("current_node children are", current_node.children)
                to_add = ejected_item[0]
                new_node = ejected_item[1]
                old_node = ejected_item[2]
                current_node.children.insert(child_index+1,new_node)
                print("current_node children",current_node.children)
                # should now handle next_leaf when at leaf level
                #if old_node.is_leaf:
                #   old.node.next_leaf = new_node

                current_node.keys.append(to_add)
                keys = current_node.keys
                index = len(keys) - 1
                while index > 0 and keys[index] < keys[index - 1]:
                    keys[index], keys[index - 1] = keys[index - 1], keys[index]
                    index -= 1
                # if number of keys is greater than maximum number of keys, eject middle key to parent
                if len(keys) >= self.order:
                    print("current node full, ejecting")
                    print("current node before ejection:",current_node)
                    mid = len(keys) // 2
                    #eject = keys.pop(len(keys)//2)
                    eject = keys[mid]
                    print("ejecting*****",eject)
                    new_node = B_plus_tree_node(False)
                    new_node.keys = keys[mid+1:]
                    new_node.children = current_node.children[mid+1:]
                    current_node.keys = keys[0:mid]
                    current_node.children = current_node.children[0:mid+1]
                    print("new node (right)",new_node)
                    print("old node (left)",current_node)
                    return (eject, new_node, current_node)
                else:
                    return None

    def delete(self, item):

        if self.is_empty():
            raise ValueError("Tree is empty!")
        else:
            current_node = self.root
            key_changes = self._delete_helper(current_node, item)
            self.size -= 1

    # first attempt at delete oh lawdy this sucks
    '''
    def _delete_helper(self, current_node, item):

        if current_node.is_leaf:

            removed = None
            for i in range(len(current_node.keys)):
                if current_node.keys[i] == item:
                    removed = current_node.keys.pop(i)
                    break
            # no item removed, item not in tree
            if removed == None:
                print("value not found")
                return (None, False)
                #raise ValueError(item, "not in tree!")

            else:
                # check if work needs to be done to fix tree
                if len(current_node.keys) == 0:
                    return (removed, True)
                else:
                    return (removed, False)

        else:
            child_index = len(current_node.keys)
            for i in range(len(current_node.keys)):
                #print("item:",item,"key:",current_node.keys[i])
                if item <= current_node.keys[i]:
                    #print(item," is less than",current_node.keys[i])
                    child_index = i
                    break
            print("child index is",child_index, "node will be",current_node.children[child_index])
            child_node = current_node.children[child_index]
            returned_value = self._delete_helper(child_node, item)
            if returned_value[1] == False:
                if returned_value[0] in current_node.keys:
                    # need to change index keys in current_node to fix tree structure
                    print("why is this so hard")
                return None
            else:
                if child_node.is_leaf:
                    # need to fix tree, start by checking siblings
                    left_sibling = current_node.children[child_index - 1] if child_index > 0 else None
                    if left_sibling:
                        if len(left_sibling.keys) >= 2:
                            # left sibling has enough to steal from
                            value = left_sibling.keys.pop()
                            child_node.keys.insert(0,value)
                            current_node.keys[child_index - 1] = value
                            return (removed, False)
                    right_sibling = current_node.children[child_index + 1] if child_index < len(current_node.children) - 1 else None
                    if right_sibling:
                        if len(right_sibling.keys) >= 2:
                            # left sibling has enough to steal from
                            value = right_sibling.keys.pop(0)
                            child_node.keys.append(value)
                            current_node.keys[child_index] = value
                            return (removed, False)
                    # no siblings can give value, merging necessary'''



def test_bptree():

    tree = B_plus_tree(5)
    items = [40,30,20,50,60,10,70,80,15,25,45,85]
    for item in items:
        print("inserting", item)
        tree.insert(item)
        print("root",tree.root)
        print("children",len(tree.root.children))
        for child in tree.root.children:
            print(child)
            print("children are",child.children)
            for child2 in child.children:
                print(child2)
                print("next leaf is",child2.next_leaf)
            print("next leaf is",child.next_leaf)

    print("\n\n *********** DONE INSERTING")
    print(tree.contains(60))
    print(tree.contains(40))
    print(tree.contains(75))
    print(tree.all_values())
    tree.delete(40)

if __name__ == '__main__':
    test_bptree()
