from bisect import bisect_left


class SegmentTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        self.tree = [float('inf')] * (4 * self.n) 
        self.baskets = baskets
        self.build(1, 0, self.n - 1) # node is current node. if index 1 is root then 2 and 3 are children

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.baskets[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def _query(self, node, start, end, x):
        if x > self.tree[node]:
            return -1 # cannot find anything more than x
        if start == end:
            return start
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        if self.tree[left_child] >= x:
            return self._query(left_child, start, mid, x)
        else:
            return  self._query(right_child, mid + 1, end, x)

    def query(self, x):
        return self._query(1, 0, self.n - 1, x)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.baskets[start] = val
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        if start <= idx <= mid:
            self._update(left_child, start, mid, idx, val)
        else:
            self._update(right_child, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])
    def update(self, index, val):
        self._update(1, 0, self.n - 1,  index, val)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = N = len(baskets)
        st = SegmentTree(baskets)
        print(st.tree)
        for f in fruits:
            index = st.query(f)
            print(index)
            if index != -1:
                unplaced -= 1
                st.update(index, 0)
        return unplaced
