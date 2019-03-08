
import time
import random

class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):

        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx+1
        return False

    def bsearch(self, val): #binary search algorithm
        lo = 0
        hi = len(self.array)-1
        bool = False

        while lo <= hi and not bool:
            mid = int((lo+hi)/2)
            if self.array[mid] == val:
                bool = True
            else:
                if val < self.array[mid]:
                    lo = mid-1
                else:
                    hi = mid + 1
        return bool

    def delete(self, val):
        if self is None:
            return None
        if val < self.val:
            self.left = self.left.delete(val)
        elif val >self.val:
            self.right = self.right.delete(val)
        else:
            #with 1 child
            if self.left is None:
                new = self.right
                self = None
                return new
            elif self.right is None:
                new = self.left
                self = None
                return new
            #with two children
            new = self.minNode(self.right)
            self.val = new.val
            self.right = self.right.delete(new.val)
            return self

        def minNode(self, node):
            current = node
            while (current.left is not None):
                current = current.left
                return current

class BST_Node: #binary search tree algorithm
    def __init__(self, val): #constructor that creates a node with data val.
        self.val = val
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val): #inserts date in a new node
        if (self.root is None):
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current.val:
            if val <= current.val:
                if current.left is None:
                    current.left = BST_Node(val)
                else:
                    self.insertNode(current.left, val)
            elif val > current.val:
                    if self.right is None:
                        current.right = BST_Node(val)
                    else: self.insertNode(current.right, val)
        else: current.right = BST_Node(val)


    def bsearch(self, val):
        return self.searchNode(self.root, val)


    def searchNode(self, current, val):
        if(current is None):
            return False
        elif(current.val == val):
            return True
        elif(current.val > val):
            return self.bsearch(current.left, val)
        else: return self.bsearch(current.right,val)

    def delete(self, val):
     if self.root is not None:
         return self.root.delete(val)

class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color
        self.parent =None


RED = True
BLACK = False


class RBBST: #red black tree algorithm
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        return current.RED

    def rotate_left(self, current):
        sister = current.right
        current.right = sister.left

        if sister.left != None:
            sister.left.parent = current
        sister.parent = current.parent
        if current.parent == None:
            self.root = sister
        else:
            if current == current.parent.left:
                current.parent.left = sister
            else:
                current.parent.right = sister
        sister.left = current
        current.parent = sister

    def rotate_right(self, current):
        sister = current.left
        current.left = sister.right

        if sister.right != None:
            sister.right.parent = current
        sister.parent = current.parent
        if current.parent == None:
            self.root = sister
        else:
            if current == current.parent.right:
                current.parent.right = sister
            else:
                current.parent.left = sister
        sister.right = current
        current.parent = sister

    def flip_colors(self, current):

        return False

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        return False

    def bsearch(self, val):

        return False

    def searchNode(self, current, val):

        return False

if __name__ == "__main__":


    set_sz = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_sz)

    for idx in range(set_sz - 1):

        tut.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))

    tut_rb = RBBST()

    for idx in range(set_sz - 1):

        tut_rb.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))