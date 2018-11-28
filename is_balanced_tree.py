class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):

    if not root:
        return 0

    left = 1 + max_depth(root.left)
    right = 1 + max_depth(root.right)
    
    return(max([left, right]))

def min_depth(root):
    if not root:
        return 0

    left = 1 + min_depth(root.left)
    right = 1 + min_depth(root.right)
    
    return(min([left, right]))

def is_balanced(node):

    biggest = max_depth(node)
    smallest = min_depth(node)

    if biggest - smallest > 1:
        return False

    return True


root_1 = TreeNode(3)
node_1 = TreeNode(9)
node_2 = TreeNode(20)
node_3 = TreeNode(15)
node_4 = TreeNode(7)
root_1.left = node_1
root_1.right = node_2
node_2.left = node_3
node_2.right = node_4

root_2 = TreeNode(1)
node_5 = TreeNode(2)
node_6 = TreeNode(2)
node_7 = TreeNode(3)
node_8 = TreeNode(3)
node_9 = TreeNode(4)
node_10 = TreeNode(4)
root_2.left = node_5
root_2.right = node_6
node_5.left = node_7
node_5.right = node_8
node_7.left = node_9
node_7.right = node_10

assert(max_depth(root_2)==4)
assert(min_depth(root_2)==2)
assert(is_balanced(root_2)==False)


assert(max_depth(root_1)==3)
assert(min_depth(root_1)==2)
assert(is_balanced(root_1)==True)


