#!python3

from B_plus_tree import B_plus_tree, B_plus_tree_node
import unittest


class BPlusTreeTest(unittest.TestCase):

    def test_init_and_properties(self):
        tree = B_plus_tree()
        # Verify tree size property
        assert isinstance(tree.size, int)
        assert tree.size == 0
        assert tree.order == 4
        # Verify root node
        assert tree.root == None

    def test_insert(self):
        tree = B_plus_tree()
        items = [40,30,20]
        # Verify tree size property
        assert isinstance(tree.size, int)
        assert tree.size == 0
        assert tree.order == 4
        # Verify root node
        assert tree.root == None
        for item in items:
            tree.insert(item)
            assert isinstance(tree.root, B_plus_tree_node)
            assert item in tree.root.keys
            assert sorted(tree.root.keys) == tree.root.keys
            assert tree.size == len(tree.root.keys)

    def test_insert_with_ejections(self):
        tree = B_plus_tree()
        items = [40,30,20]
        next_items = [50,60,10,70,80,15,25,45,85]
        # Verify tree size property
        assert isinstance(tree.size, int)
        assert tree.size == 0
        assert tree.order == 4
        tree_size = 0
        # Verify root node
        assert tree.root == None
        for item in items:
            tree.insert(item)
            assert isinstance(tree.root, B_plus_tree_node)
            assert item in tree.root.keys
            assert sorted(tree.root.keys) == tree.root.keys
            assert tree.size == len(tree.root.keys)
            tree_size += 1
            assert tree.size == tree_size

        for item in next_items:
            tree.insert(item)
            tree_size += 1
            assert tree.size == tree_size
            assert len(tree.root.keys) < tree.order
            assert len(tree.root.keys) == len(tree.root.children) - 1
            for child in tree.root.children:
                assert len(child.keys) < tree.order
                # test if leaf have no children or non leaf node has proper number of keys and children
                assert child.is_leaf and len(child.children) == 0 or len(child.keys) == len(child.children) - 1

        assert tree.root.keys == [60]
        assert len(tree.root.children) == 2
        assert tree.root.children[0].keys == [20,40]
        assert tree.root.children[1].keys == [80]
        assert tree.all_values() == [10,15,20,25,30,40,45,50,60,70,80,85]

    def test_insert_with_repeated_values(self):
        tree = B_plus_tree()
        items = [40,30,20,50,60,10,70,80,15,25,45,85,40]
        for item in items:
            tree.insert(item)

        assert tree.root.keys == [60]
        assert tree.root.children[0].keys == [20,30,40]
        assert tree.root.children[0].children[2].keys == [30,40]
        assert tree.root.children[0].children[3].keys == [40,45,50]
        assert tree.all_values() == [10,15,20,25,30,40,40,45,50,60,70,80,85]

        tree.insert(40)
        tree.insert(40)
        assert tree.root.keys == [40,60]
        assert tree.root.children[0].keys == [20,30]
        assert tree.root.children[1].keys == [40]
        assert tree.root.children[2].keys == [80]
        assert tree.root.children[0].children[2].keys == [30,40]
        assert tree.root.children[1].children[0].keys == [40,40]
        assert tree.root.children[1].children[1].keys == [40,45,50]
        assert tree.all_values() == [10,15,20,25,30,40,40,40,40,45,50,60,70,80,85]

    def test_contains(self):
        tree = B_plus_tree()
        items = [40,30,20,50,60,10,70,80,15,25,45,85]
        for item in items:
            tree.insert(item)

        for item in items:
            assert tree.contains(item)

        assert tree.contains(11) == False
        assert tree.contains(101) == False
        assert tree.contains(51) == False

    def test_all_values(self):
        tree = B_plus_tree()
        items = [40,30,20,50,60,10,70,80,15,25,45,85]
        i = 0
        for item in items:
            i += 1
            tree.insert(item)
            assert tree.all_values() == sorted(items[:i])

    def test_order_5(self):

        tree = B_plus_tree(5)
        items = [40,30,20,50,60,10,70,80,15,25,45,85]
        i = 0
        for item in items:
            i += 1
            tree.insert(item)
            assert len(tree.root.keys) < 5
            assert tree.root.is_leaf and len(tree.root.children) == 0 or len(tree.root.keys) == len(tree.root.children) - 1
            assert tree.all_values() == sorted(items[:i])

        assert tree.root.keys == [20,40,60]
        assert tree.root.children[0].keys == [10,15]
        assert tree.root.children[1].keys == [20,25,30]
        assert tree.root.children[2].keys == [40,45,50]
        assert tree.root.children[3].keys == [60,70,80,85]


if __name__ == '__main__':
    unittest.main()
