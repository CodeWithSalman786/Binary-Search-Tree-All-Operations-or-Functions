# Author: @CodeWithSalman
# ------ BINARY TREE ALL FUNCTIONS OR OPERATIONS ------ #
# DECLARING TreeNode CLASS.
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
# INSERT FUNCTION.
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
# PRINTING INITIAL TREE VALUES.
def display(root):
    return inorder(root)
# INORDER NODE DISPLAY FUNCTION.
def inorder(root):
    # USE OF LIST.
    result = []
    # USE OF LIST.
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            # MOVING TO THE LEFT SIDE OF TREE.
            current = current.left
        # POPPING OR REMOVING ELEMENT FROM STACK.
        current = stack.pop()
        # STORING ELEMENT IN THE RESULT LIST[] AFTER POPPING FROM STACK.
        result.append(current.val)
        # MOVING TO THE RIGHT SIDE OF TREE.
        current = current.right
    return result
# PREORDER NODE DISPLAY FUNCTION.
def preorder(root):
    # USE OF LIST.
    result = []
    # USE OF LIST.
    stack = [root]
    while stack:
        # POPPING OR REMOVING ELEMENT FROM STACK.
        current = stack.pop()
        if current:
            # STORING ELEMENT IN THE RESULT LIST[] AFTER POPPING FROM STACK.
            result.append(current.val)
            # APPENDING ALL THE LEFT NODES IN THE STACK.
            stack.append(current.left)
            # APPENDING ALL THE RIGHT NODES IN THE STACK NOW.
            stack.append(current.right)
    return result
# POSTORDER NODE DISPLAY FUNCTION.
def postorder(root):
    # USE OF LIST.
    result = []
    # USE OF LIST.
    stack = [root]
    while stack:
        # POPPING OR REMOVING ELEMENT FROM THE STACK.
        current = stack.pop()
        if current:
            # STORING ELEMENT IN THE RESULT LIST[] AFTER POPPING FROM STACK.
            result.insert(0, current.val)
            # APPENDING ALL THE LEFT NODES IN THE STACK.
            stack.append(current.left)
            # APPENDING ALL THE RIGHT NODES IN THE STACK.
            stack.append(current.right)
    return result
# MAXIMUM VALUE FUNCTION.
def max_Value(root):
    while root.right:
        root = root.right
    return root
# MINIMUM VALUE FUNCTION.
def min_Value(root):
    while root.left:
        root = root.left
    return root
# DELETE FUNCTION.
def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = min_Value(root.right).val
        root.right = delete(root.right, root.val)
    return root
# UPDATE FUNCTION.
def update(root, old, new):
    root = delete(root, old)
    root = insert(root, new)
    return root
# SEARCH FUNCTION.
def search(root, key):
    while root is not None:
        if root.val == key:
            print("Found")
            return
        elif key < root.val:
            root = root.left
        elif key > root.val:
            root = root.right
    print("No Found")
    return root
# HEIGHT OF TREE FUNCTION.
def tree_Height(root):
    if root is None:
        return -1
    left_Height = tree_Height(root.left)
    right_Height = tree_Height(root.right)
    return 1 + max(left_Height, right_Height)
# TOTAL NODES FUNCTION.
def total_Nodes(root):
    if root is None:
        return 0
    else:
        return 1 + total_Nodes(root.left) + total_Nodes(root.right)
# ---------------- MAIN CODE OR DRIVER CODE. --------------- #
# MAIN CODE OR DRIVER CODE.
if __name__ == '__main__':
    root = None
    # WHILE TRUE HERE FOR AGAIN AND AGAIN REPETITION.
    # keys = [33, 22, 44, 55, 66]
    # for key in keys:
    #     root = insert(root, key)
    while True:
        print("1 = INSERT NODE")
        print("2 = INORDER NODE DISPLAY")
        print("3 = PREORDER NODE DISPLAY")
        print("4 = POSTORDER NODE DISPLAY")
        print("5 = UPDATE NODE")
        print("6 = SEARCH NODE")
        print("7 = DELETE NODE")
        print("8 = MAX VALUE")
        print("9 = MIN VALUE")
        print("10 = HEIGHT OF TREE")
        print("11 = PRINT TREE")
        print("12 = TOTAL NODES")
        print("13 = EXIT OR ESCAPE")
        # NOW LET'S INPUT SELECTION FROM USER.
        selection = int(input("Make any One Selection from Above: "))
        if selection == 1:
            key = int(input("Enter the Number to Store: "))
            root = insert(root, key)
        elif selection == 2:
            print("Inorder: ", inorder(root))
        elif selection == 3:
            print("Preorder: ", preorder(root))
        elif selection == 4:
            print("Postorder: ", postorder(root))
        elif selection == 5:
            old = int(input("Enter the Old Value: "))
            new = int(input("Enter the New Value: "))
            update(root, old, new)
        elif selection == 6:
            key = int(input("Enter the value to Search: "))
            search(root, key)
        elif selection == 7:
            key = int(input("Enter the value to Delete: "))
            delete(root, key)
        elif selection == 8:
            maximum = max_Value(root).val
            print("Maximum Value: ", maximum)
        elif selection == 9:
            minimum = min_Value(root).val
            print("Minimum Value: ", minimum)
        elif selection == 10:
            print("Height of Tree: ", tree_Height(root))
        elif selection == 11:
            print("Initial Tree: ", display(root))
        elif selection == 12:
            print("Total Nodes: ", total_Nodes(root))
        elif selection == 13:
            exit()
