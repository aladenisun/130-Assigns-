# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
import matplotlib.pyplot as plt

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

        # self.id = [random.randint(0, N - 1) for i in range(N)]

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

            for j_idx in range(i_idx + 1, len(self.id)):

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp

        return self.id

    @property
    def insertion_sort(self):

        for i_idx in range(1, len(self.id)):
            value = self.id[i_idx]
            j_idx = i_idx - 1
            while j_idx >= 0 and value < self.id[j_idx]:
                self.id[j_idx + 1] = self.id[j_idx]
                j_idx = j_idx - 1
                self.id[j_idx + 1] = value

        return self.id

    @property
    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).
        """

        mid = int(len(self.id) / 2)
        while mid > 0:
            for i_idx in range(mid, len(self.id), 1):
                j_idx = i_idx
                temp = self.id[i_idx]
                while j_idx >= mid and self.id[j_idx - mid] > temp:
                    self.id[j_idx] = self.id[j_idx - mid]
                    j_idx = j_idx - mid
                self.id[j_idx] = temp
            mid = int(mid / 2)
        return self.id

    def sink(self, N, i):
        max = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        if not N <= left and self.id[i] < self.id[left]:
            max = left

        if not right >= N and self.id[max] < self.id[right]:
            max = right

        if max != i:
            [self.id[i], self.id[max]] = (self.id[max], self.id[i])
            self.sink(N, max)

            return self.id

    def heap_sort(self):
        N = len(self.id)
        for i_idx in range(N, -1, -1):
            self.sink(N, i_idx)

        for i_idx in range(N - 1, 0, -1):
            self.id[i_idx], self.id[0] = self.id[0], self.id[i_idx]
            self.sink(i_idx, 0)

        return self.id

    def merge(self, l, r):
        if len(l) == 0:
            return r
        if len(r) == 0:
            return l

        array = []
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                self.id[k] = l[i]
                i = i+1
            else:
                self.id[k] = r[j]
                j = j+1

        k = k+1

        while(j<len(l)):
            self.id[k] = l[i]
            i = i+1
            k = k+1

        while (j < len(r)):
            self.id[k] = r[j]
            j = j=1
            k= k+1

    def merge_sort(self, arr_):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        :param arr_:
        """

        if len(self.id) == 0: return self.id[:len(self.id)]
        if len(self.id) == 1: return self.id[:len(self.id)]

        mid = int(len(self.id)/2)
        arr1 = self.id[0:mid]
        arr2 = self.id[mid:len(self.id)]

        new_arr1 = self.merge_sort(arr2)
        new_arr2 = self.merge_sort(arr2)
        newArr = self.merge(new_arr1,new_arr2)

        return newArr

    def partition (self, low, high):
        i = (low-1)
        pivot = self.id[high]

        for j in range (low, high):
            if self.id[j] <= pivot:
                i = i+1
                self.id[i], self.id[j] = self.id[i], self.id[j]

                self.id[i+1], self.id[high] = self.id[high], self.id[i+1]
                return (i+1)



    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.
        """
        low = 0
        high = len(self.id)-1
        if low < high:
            pivot = self.partition(low, high)

            self.quick_sort(low, pivot-1)
            self.quick_sort(pivot+1, high)

        return self.id

        # this plots things in log scale (pls google it), you need to add matplotlib
        # to your virtualenv first!

        # plot also python's sorted() function to see how well you do.

        # SELECTION SORT
        # iteration
        set_szs = [10, 100, 1000, 10000]
        set_szs = [7, 8, 9]
        timing = []

        # gives the timing for union operation only, you might want to do this for all functions you wrote.
        for set_sz in set_szs:
            # initialize network nodes
            inodes = UF()
            inodes.qf_init(set_sz)

            t0 = time.time()

            for idx in range(set_sz - 1):
                rp = random.randint(0, set_sz - 1)
                rq = random.randint(0, set_sz - 1)
                inodes.selection_sort(rp, rq)

            t1 = time.time()

            total_time = t1 - t0

            timing.append(total_time)

            print(total_time)

        plt.plot(set_szs, timing)

        # INSERTION SORT
        # iteration
        set_szs = [10, 100, 1000, 10000]
        set_szs = [7, 8, 9]
        timing = []

        # gives the timing for union operation only, you might want to do this for all functions you wrote.
        for set_sz in set_szs:
            # initialize network nodes
            inodes = UF()
            inodes.qf_init(set_sz)

            t0 = time.time()

            for idx in range(set_sz - 1):
                rp = random.randint(0, set_sz - 1)
                rq = random.randint(0, set_sz - 1)
                inodes.insertion_sort(rp, rq)

            t1 = time.time()

            total_time = t1 - t0

            timing.append(total_time)

            print(total_time)

        plt.plot(set_szs, timing)

        #SHELL SORT
        # iteration
        set_szs = [10, 100, 1000, 10000]
        set_szs = [7, 8, 9]
        timing = []

        # gives the timing for union operation only, you might want to do this for all functions you wrote.
        for set_sz in set_szs:
            # initialize network nodes
            inodes = UF()
            inodes.qf_init(set_sz)

            t0 = time.time()

            for idx in range(set_sz - 1):
                rp = random.randint(0, set_sz - 1)
                rq = random.randint(0, set_sz - 1)
                inodes.shell_sort(rp, rq)

            t1 = time.time()

            total_time = t1 - t0

            timing.append(total_time)

            print(total_time)

        plt.plot(set_szs, timing)

        #HEAP SORT
        # iteration
        set_szs = [10, 100, 1000, 10000]
        set_szs = [7, 8, 9]
        timing = []

        # gives the timing for union operation only, you might want to do this for all functions you wrote.
        for set_sz in set_szs:
            # initialize network nodes
            inodes = UF()
            inodes.qf_init(set_sz)

            t0 = time.time()

            for idx in range(set_sz - 1):
                rp = random.randint(0, set_sz - 1)
                rq = random.randint(0, set_sz - 1)
                inodes.heap_sort(rp, rq)

            t1 = time.time()

            total_time = t1 - t0

            timing.append(total_time)

            print(total_time)

        plt.plot(set_szs, timing)

        #MERGE SORT
        # iteration
        set_szs = [10, 100, 1000, 10000]
        set_szs = [7, 8, 9]
        timing = []

        # gives the timing for union operation only, you might want to do this for all functions you wrote.
        for set_sz in set_szs:
            # initialize network nodes
            inodes = UF()
            inodes.qf_init(set_sz)

            t0 = time.time()

            for idx in range(set_sz - 1):
                rp = random.randint(0, set_sz - 1)
                rq = random.randint(0, set_sz - 1)
                inodes.merge_sort(rp, rq)

            t1 = time.time()

            total_time = t1 - t0

            timing.append(total_time)

            print(total_time)

        plt.plot(set_szs, timing)

        #QUICK SORT
        # iteration
        set_szs = [10, 100, 1000, 10000]
        set_szs = [7, 8, 9]
        timing = []

        # gives the timing for union operation only, you might want to do this for all functions you wrote.
        for set_sz in set_szs:
            # initialize network nodes
            inodes = UF()
            inodes.qf_init(set_sz)

            t0 = time.time()

            for idx in range(set_sz - 1):
                rp = random.randint(0, set_sz - 1)
                rq = random.randint(0, set_sz - 1)
                inodes.quick_sort(rp, rq)

            t1 = time.time()

            total_time = t1 - t0

            timing.append(total_time)

            print(total_time)

        plt.plot(set_szs, timing)


        # plt.plot(set_szs, timing)
        # plt.xscale('log')
        # plt.yscale('log')
        # plt.title('log')
        # plt.ylabel('some numbers')
        # plt.show()

        pass
