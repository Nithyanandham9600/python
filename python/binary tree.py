class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    elif value < root.data:
        return search(root.left, value)
    else:
        return search(root.right, value)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def swap_nodes(root):
    if root:
        root.left, root.right = root.right, root.left
        swap_nodes(root.left)
        swap_nodes(root.right)

def merge_trees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.data = t2.data
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1

root1 = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root1 = insert(root1, val)
print("Inorder:")
inorder (root1)
print("\nSearch 40:", search (root1, 40))
print("Search 100:", search (root1, 100))
print("Height:", height (root1))
swap_nodes (root1)
print("Inorder after swap:")
inorder (root1)