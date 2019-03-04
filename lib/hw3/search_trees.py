
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



        return False

    def bsearch(self, val):

        return False

    def searchNode(self, current, val):

        return False
    def delete(self, val):
        return False



class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color


RED = True
BLACK = False


class RBBST: #red black tree algorithm
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):



        return False

    def rotate_left(self, current):



        return False

    def rotate_right(self, current):

        return False

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