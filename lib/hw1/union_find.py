

# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import time
import random
import matplotlib.pyplot as plt
#import self as self


class UF(object):
    """Union Find class
    """

    def __init__(self):
        self.id = []
        self.sz = []

    def qf_init(self, N):
        """initialize the data structure
        """
        for x in range(N):
            self.id.append(x)

        for x in range(N):
            self.sz.append(1)


    def qf_union(self, p, q):
        """"Union operation for Quick-Find Algorithm.
        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)
        """
        pID = self.id[p]

        for x in range(len(self.id)):
            if self.id[x] == pID:
                self.id[x] = self.id[q]
        return 1

    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected
        """
        return self.id[p] == self.id[q]
        #return self.id[p] == self.id[q]


    def qu_findroot(self, x):
        if x != self.id[x]: self.id[x] = self.qu_findroot(self.id[x])
        return self.id[x]

    def pqu_findroot(self, x):
        while x != self.id[x]:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        else: return x

    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.
         """
        pID = self.qu_findroot(p)
        qID = self.qu_findroot(q)

        if pID == qID: return

        if p > q: self.id[qID] = pID
        else: self.id[pID] = qID
        return 1

    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected
         """
        pID = self.qu_findroot(p)
        qID = self.qu_findroot(q)
        return pID == qID


    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.
         """
        pID = self.qu_findroot(p)
        qID = self.qu_findroot(q)

        if pID == qID: return
        if(self.sz[pID] < self.sz[qID]):
            self.id[pID] = qID
            self.sz[qID] += self.sz[pID]
        else:
            self.id[qID] = pID
            self.sz[pID] += self.sz[qID]
        return 1


    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected
         """
        pID = self.qu_findroot(p)
        qID = self.qu_findroot(q)
        return pID == qID


    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        pID = self.pqu_findroot(p)
        qID = self.pqu_findroot(q)

        if pID == qID: return

        if p > q:
            self.id[qID] = pID
        else:
            self.id[pID] = qID
        return 1


    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected
         """
        pID = self.pqu_findroot(p)
        qID = self.pqu_findroot(q)
        return pID == qID

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.
         """
        pID = self.pqu_findroot(p)
        qID = self.pqu_findroot(q)

        if pID == qID: return
        if (self.sz[pID] < self.sz[qID]):
            self.id[pID] = qID
            self.sz[qID] += self.sz[pID]
        else:
            self.id[qID] = pID
            self.sz[pID] += self.sz[qID]
        return 1


    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected
         """
        pID = self.pqu_findroot(p)
        qID = self.pqu_findroot(q)
        return pID == qID


if __name__ == "__main__":

    # QUICK FIND
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
            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    plt.plot(set_szs, timing)

    # UNION FIND
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
            inodes.qu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    plt.plot(set_szs, timing)

    #WEIGHTED UNION
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
            inodes.wqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    plt.plot(set_szs, timing)


    #COMPRESSED UNION
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
            inodes.pqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    plt.plot(set_szs, timing)

    #WEIGHTED COMPRESSED UNION
    # iteration
    set_szs = [10, 100, 1000, 10000]
    set_szs = [7, 8, 9]
    set_sz = [7, 8, 9]
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
            inodes.wpqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    plt.plot(set_szs, timing)

    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()