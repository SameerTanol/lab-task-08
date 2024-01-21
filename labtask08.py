
# Q1: Write a function to search for a value in a BST.

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search_bst(root, key):
    if not root or root.val == key:
        return root
    if root.val < key:
        return search_bst(root.right, key)
    return search_bst(root.left, key)


# Q2: Implement a function to delete a node from a BST.


def delete_node(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current


# Q3: Create a function to find the minimum and maximum values in a BST.

def find_min_value(root):
    current = root
    while current.left:
        current = current.left
    return current.val

def find_max_value(root):
    current = root
    while current.right:
        current = current.right
    return current.val


#Q4: Write a function to find the in-order successor and predecessor of a node in a BST.

def find_inorder_successor_predecessor(root, key):
    successor = None
    predecessor = None

    while root:
        if key < root.val:
            successor = root
            root = root.left
        elif key > root.val:
            predecessor = root
            root = root.right
        else:
            if root.right:
                successor = find_min(root.right)
            if root.left:
                predecessor = find_max(root.left)
            break

    return successor, predecessor

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

def find_max(node):
    current = node
    while current.right:
        current = current.right
    return current


#Q5: Implement a function to find the k-th smallest element in a BST.

def kth_smallest_element(root, k):
    stack = []
    count = 0
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        current = current.right

    return None
