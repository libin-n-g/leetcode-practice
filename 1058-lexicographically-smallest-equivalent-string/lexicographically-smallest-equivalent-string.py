class UnionFind:
    def __init__(self, elements=None):
        # Initialize the parent dictionary; each element is its own parent initially
        self.parent = {}
        if elements is not None:
            for element in elements:
                self.parent[element] = element
    
    def find(self, i):
        # Ensure the element exists in the parent dictionary
        if i not in self.parent:
            self.parent[i] = i
            return i
        # Traverse the parent dictionary until the root is found
        path = []
        current = i
        while self.parent[current] != current:
            path.append(current)
            current = self.parent[current]
        # Path compression: make all nodes in the path point to the root
        for node in path:
            self.parent[node] = current
        return current
    
    def union(self, i, j):
        # Find representatives of sets containing i and j
        irep = self.find(i)
        jrep = self.find(j)
        # If representatives are different, make j's representative the parent of i's representative
        if irep >= jrep:
            self.parent[irep] = jrep
        else:
            self.parent[jrep] = irep
            # self.parent[jrep] = min(jrep, irep)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        char_map = UnionFind()
        for c1, c2 in zip(s1, s2):
            char_map.union(c1, c2)
        ret = ''
        for s in baseStr:
            ret += char_map.find(s)
        return ret
