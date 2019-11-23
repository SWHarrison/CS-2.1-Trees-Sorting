#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        node = self._find_node(string)
        print(node)
        if node and node[0].terminal and node[1] == string:
            return True
        return False

    #previous faulty version
    def bad_insert(self, string):
        # Scenarios: 1. no child for that character 2. full match 3. partial match
        # 1. Add suffix as new child (example: adding 'Skylar' to an 'S' node with no 'k' children)
        # 2. Add node in after match
        # 3. Break the child node into two parts wherever the split occurs
        # Example: Adding 'Sasha' to 'S' -> 'am'
        # Break 'am' into 'a' -> 'm', with 'm' keeping all of previous 'am' 's childrien
        # New paths are 'S' -> 'A' -> 'Sha' and S -> 'A' -> 'M'
        """Insert the given string into this prefix tree."""
        current_node = self.root
        current_string = string[:]
        while current_string[0] in current_node.children:

            print(current_node)
            current_node = current_node.children[current_string[0]]
            print("current_node is now",current_node)
            print("comparing",current_node,string)
            no_match_index = 1
            for i in range(1,min(len(current_string),len(current_node.full_path))):
                if current_string[i] == current_node.full_path[i]:
                    no_match_index += 1
                else:
                    break

            if no_match_index < len(current_node.full_path):

                print("partial match, fail at index",no_match_index)
                # use index of where new string and old string diverge to get new paths
                new_split_string = current_string[0:no_match_index]
                remainder = current_string[no_match_index:]
                old_remainder = current_node.full_path[no_match_index:]
                #current node's new path is
                current_node.full_path = new_split_string
                current_node.terminal = False
                # old child getting new assignment if necessary
                print("current_node",current_node)
                print("current_node children",current_node.children)
                split_child = PrefixTreeNode(old_remainder)
                # if old children exists then old child split due to new string
                if current_node.full_path[0] in current_node.children:
                    print("##@#@$%%@@old child exists")
                    old_child_children = old_child.children
                    split_child.terminal = old_child.terminal
                    split_child.children = old_child_children
                else:
                    split_child.terminal = True

                # Remove old child, add new child
                #current_node.children[current_string[0]] = None
                #current_node.children.pop(current_string[0])
                current_node.children[old_remainder[0]] = split_child
                # add new node
                new_child = PrefixTreeNode(remainder)
                new_child.terminal = True
                current_node.children[remainder[0]] = new_child
                print("***********")
                print("new node at this point is",current_node)
                print("children at",current_node.children)
                for child in current_node.children:
                    print(child)
                    print(current_node.children[child].terminal)
                print("***********")
                self.size += 1
                return

            elif no_match_index == len(current_node.full_path):

                print("full match")
                current_node = current_node.children[current_string[no_match_index]]
                current_string = current_string[no_match_index:]

        # at node to insert at after while loop
        print("arrived at final parent node",current_node)
        print("string is",current_string)
        current_string = current_string[len(current_node.full_path):]
        new_node = PrefixTreeNode(current_string)
        new_node.terminal = True
        current_node.children[current_string[0]] = new_node
        print("***********")
        print("current_node is",current_node)
        print("children at",current_node.children)
        print("***********")
        self.size += 1

    def insert(self, string):

        current_node = self.root
        current_string = string[:]
        while True:
            #print("comparing",current_node.full_path,"to",current_string)
            #print("comparing",current_node.children,"to",current_string)
            try:
                current_node = current_node.children[current_string[0]]
                #print("child exists for",current_string[0],"moving to that node")
            except KeyError:
                # No more matching edges, add new node
                #print("child does NOT exist for",current_string[0],"creating that node")
                new_node = PrefixTreeNode(current_string)
                new_node.terminal = True
                current_node.add_child(current_string[0], new_node)
                self.size += 1
                return

            #print("checking for partial match for",current_node.full_path,"to",current_string)
            # Perfect match, make terminal if not already
            if current_string == current_node.full_path:
                #print("node is terminal:",current_node.terminal)
                if(current_node.terminal == False):
                    self.size += 1
                current_node.terminal = True
                return

            first_mismatch_index = 1
            for i in range(1, min(len(current_string), len(current_node.full_path))):
                if (current_string[i] == current_node.full_path[i]):
                    first_mismatch_index += 1

            #print("first_mismatch_index is",first_mismatch_index)

            # String partially matches to an existing node
            if len(current_string) < len(current_node.full_path) or first_mismatch_index < len(current_node.full_path):
                #print("partial match, fail at index",first_mismatch_index)
                # child_1 is modified old child or new child that follows old path
                # child_2 is new child with remainder of string
                new_path = current_node.full_path[0:first_mismatch_index]
                child_1_path = current_node.full_path[first_mismatch_index:]
                child_2_path = current_string[first_mismatch_index:]
                # set up new nodes and paths
                current_node.full_path = new_path
                child_1 = PrefixTreeNode(child_1_path)
                child_1.terminal = current_node.terminal
                # transfer current_node's previous children to child_1
                #print("current_node is",current_node)
                #print("children are",current_node.children)
                to_remove = []
                for key in current_node.children:
                    child_1.children[key] = current_node.children[key]
                    to_remove.append(key)
                for item in to_remove:
                    del current_node.children[item]
                # add children to current_node
                current_node.children[child_1_path[0]] = child_1
                if(len(child_2_path) > 0):
                    child_2 = PrefixTreeNode(child_2_path)
                    child_2.terminal = True
                    current_node.children[child_2_path[0]] = child_2
                    current_node.terminal = False
                else:
                    current_node.terminal = True

                self.size += 1
                return
            # Node continues on path
            else:
                #print("node continuing")
                current_string = current_string[first_mismatch_index:]



    def _find_node(self, string):
        """Return a tuple containing the node that terminates the given string
        in this prefix tree and the node's depth, or if the given string is not
        completely found, return None and the depth of the last matching node.
        Search is done iteratively with a loop starting from the root node."""
        # Radix tree does not have a useful depth attribute, therefore not returning it
        # Instead returning the prefix to get to the current node

        if(string == ""):
            return self.root
        path = ""
        current_node = self.root
        current_string = string[:]
        while current_node != None and len(current_string) > 0:

            if(current_string[0] in current_node.children):
                current_node = current_node.children[current_string[0]]
            else:
                return None
            path += current_node.full_path
            #print(current_node)
            if(current_node == None):
                return None
            if(current_string == current_node.full_path):
                return (current_node, path)

            last_match_index = 0
            for i in range(0, min(len(current_string),len(current_node.full_path))):
                #print(current_string[i], current_node.full_path[i])
                if current_string[i] != current_node.full_path[i]:
                    break
                last_match_index += 1

            #print("last match at index", last_match_index)
            # This means we return the current node or None
            if(len(current_string) <= len(current_node.full_path)):
                #print("current string shorter than node path")
                # current string matches full path
                if(last_match_index >= len(current_string)):
                    # therefore match and return current_node
                    return (current_node, path)
                else:
                    return None
            # else we move on or return None
            else:
                #print("current string longer than node path")
                if(last_match_index >= len(current_node.full_path)):
                    current_string = current_string[last_match_index:]
                else:
                    return None

        return None

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        start = self._find_node(prefix)
        #print("start node is", start[0])
        #print("path is",start[1])
        if start:
            self._traverse(start[0],start[1],completions.append)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        start = self.root
        if start:
            self._traverse(start,"",all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node and visit each node with the given function."""
        '''print("looking at",node)
        print("prefix is",prefix)
        print("whole word is",prefix+node.full_path)
        print("children with path",node.children)
        print("terminal:",node.terminal)'''
        if(node.terminal):
            print("adding",prefix)
            visit(prefix)
        for child in node.children:
            child = node.children[child]
            self._traverse(child,prefix + child.full_path,visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def test_1():
    tree = PrefixTree()
    tree.insert("ABC")
    tree.insert("ABD")
    tree.insert("ABDE")
    tree.insert("ACA")
    print("\n\nXXXXXXXXXXX all inserted testing")
    print(tree.root.children)
    print(tree.root.children['A'])
    print(tree.root.children['A'].children)
    print(tree.root.children['A'].children['C'])
    print(tree.root.children['A'].children['C'].children)
    print(tree.root.children['A'].children['B'])
    print(tree.root.children['A'].children['B'].children)
    print(tree.root.children['A'].children['B'].children['C'])
    print(tree.root.children['A'].children['B'].children['D'])
    print(tree.root.children['A'].children['B'].children['C'].children)
    print(tree.root.children['A'].children['B'].children['D'].children)
    print(tree.root.children['A'].children['B'].children['D'].children['E'])
    print("XXXXXXXXXXX")

    print(tree.complete("AB"))
    print(tree.strings())

if __name__ == '__main__':

    #test_1()
    tree = PrefixTree()
    to_insert = ['ABC', 'ABD', 'A', 'XYZ']
    for item in to_insert:
        print("inserting",item )
        tree.insert(item)

    print("complete: ",tree.complete("ABC"))
    print("*********")
    print("strings: ",tree.strings())
