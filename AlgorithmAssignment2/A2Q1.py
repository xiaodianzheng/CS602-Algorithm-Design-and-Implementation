import sys


class Node(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.is_root = True
        self.left_sub_nodes = 0
        self.right_sub_nodes = 0


class BinaryTree(object):
    def __init__(self, root, nodes):
        self.root = root
        self.nodes = nodes
        self.ordered_nodes = sorted(list(nodes.keys()))
        self.bst_preorder = []

    def change_into_bst(self, root):
        # inorder traversal
        if root is None:
            return
        self.change_into_bst(root.left)
        root.value = self.ordered_nodes.pop(0)
        self.change_into_bst(root.right)

    def preorder(self, root):
        # preorder traversal
        if root is None:
            return
        self.bst_preorder.append(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def calculate_sub_nodes(self, root):
        # postorder traversal
        if root is None:
            return
        self.calculate_sub_nodes(root.left)
        self.calculate_sub_nodes(root.right)
        if root.left is not None:
            root.left_sub_nodes = root.left.left_sub_nodes + root.left.right_sub_nodes + 1
        if root.right is not None:
            root.right_sub_nodes = root.right.left_sub_nodes + root.right.right_sub_nodes + 1

    def preorder_bst(self, root, ordered_nodes):
        # preorder traversal
        if root is None:
            return
        self.bst_preorder.append(ordered_nodes.pop(root.left_sub_nodes))
        self.preorder_bst(root.left, ordered_nodes)
        self.preorder_bst(root.right, ordered_nodes)


def build_mirror_bt(a):
    """
    The time complexity for this function is O(n)
    """
    nodes = {}
    for node in a:
        cur_val = int(node[0])
        if cur_val not in nodes.keys():
            nodes[cur_val] = Node(value=cur_val)
        if node[1] != 'x':
            left_value = int(node[1])
            if left_value not in nodes.keys():
                nodes[left_value] = Node(value=left_value)
            nodes[cur_val].right = nodes[left_value]
            nodes[left_value].is_root = False
        if node[2] != 'x':
            right_value = int(node[2])
            if right_value not in nodes.keys():
                nodes[right_value] = Node(value=right_value)
            nodes[cur_val].left = nodes[right_value]
            nodes[right_value].is_root = False
    for key in nodes:
        if nodes[key].is_root:
            return BinaryTree(nodes[key], nodes)


def mirror_BST(a):
    """
    The total time complexity is O(n)
    """
    bt = build_mirror_bt(a)
    # method 1
    bt.change_into_bst(bt.root)
    bt.preorder(bt.root)
    # method 2
    # bt.calculate_sub_nodes(bt.root)
    # bt.preorder_bst()
    return " ".join(str(i) for i in bt.bst_preorder)


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(mirror_BST(a))