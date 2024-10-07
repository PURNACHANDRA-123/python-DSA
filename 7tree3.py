from collections import deque

class TreeNode:  # Pre-order Traversal (Root → Left → Right)
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def BFS(node):
    if node is None:
        return

    queue = deque([node])  # Use a deque for efficient BFS

    while queue:
        current_node = queue.popleft()
        print(current_node.data, end=" ")  # Process the current node

        for child in current_node.children:  # Explore children level-by-level
            queue.append(child)

# Example tree creation (same as before)
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)

# BFS traversal
BFS(root)  # Output: A B C D E (level-order traversal)


# About using BFS and DFS together
# No, you cannot directly use BFS and DFS at the same time on the same tree traversal. They have different exploration strategies:

# - BFS explores nodes level-by-level, visiting all children of a node before moving to the next level.
# - DFS explores branches as deeply as possible, visiting all children of a node before moving to its siblings.

# However, you can use them for different purposes within the same program. Here's an example:

# 1. Use BFS to find the shortest path between two nodes in a tree.
# 2. Use DFS to check if a specific node exists in the tree.


