# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
#import matplotlib.pyplot as plt

class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []


    def sort_init(self, N):
        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')


        #self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id


    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)):

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp


        return self.id

    @property
    def insertion_sort(self):

        for i_idx in range (1, len(self.id)):
            value = self.id[i_idx]
            j_idx = i_idx-1
            while j_idx >= 0 and value < self.id[j_idx]:
                self.id[j_idx+1] = self.id[j_idx]
                j_idx = j_idx-1
                self.id[j_idx+1] = value

        return self.id

    @property
    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).
        """

        mid = int(len(self.id) / 2)
        while mid > 0:
            for i_idx in range(mid, len(self.id),1):
                j_idx = i_idx
                temp = self.id[i_idx]
                while j_idx >= mid and self.id[j_idx - mid] > temp:
                    self.id[j_idx] = self.id[j_idx - mid]
                    j_idx = j_idx-mid
                self.id[j_idx] = temp
            mid = int(mid / 2)
        return self.id

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.
        """


        return self.id

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """

        return 1

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """

        return 1


    # this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.


    # plt.plot(set_szs, timing)
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.title('log')
    # plt.ylabel('some numbers')
    # plt.show()