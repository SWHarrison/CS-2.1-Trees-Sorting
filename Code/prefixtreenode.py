#!python3


class PrefixTreeNode:
    """PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string."""

    # Choose a type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods
    CHILDREN_TYPE = dict

    def __init__(self, character=None):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""
        # Character that this node represents
        if(character):
            self.character = character[0]
            self.full_path = character
        else:
            self.character = ""
            self.full_path = ""
        # Data structure to associate character keys to children node values
        self.children = PrefixTreeNode.CHILDREN_TYPE()
        # Marks if this node terminates a string in the prefix tree
        self.terminal = False

    def is_terminal(self):
        """Return True if this prefix tree node terminates a string."""
        return self.terminal

    def num_children(self):
        """Return the number of children nodes this prefix tree node has."""
        return len(self.children.keys())

    def has_child(self, character):
        """Return True if this prefix tree node has a child node that
        represents the given character amongst its children."""
        if character in self.children:
            return True
        return False

    def get_child(self, character):
        """Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not."""
        if character in self.children:
            return self.children[character]

        raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children."""

        if character[0] in self.children:
            raise ValueError(f'Child already exists for character {character!r}')
        else:
            self.children[character[0]] = child_node

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character}),({self.full_path})'


if __name__ == '__main__':

    node1 = PrefixTreeNode("sam")
    node2 = PrefixTreeNode("sasha")

    print(node1, node2)
    node1.add_child(node2.character,node2)
