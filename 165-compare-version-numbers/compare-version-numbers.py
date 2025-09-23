class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split = version1.split(".")
        v2_split = version2.split(".")
        max_range = max(len(v1_split), len(v2_split))
        while len(v1_split) < max_range:
            v1_split.append(0)
        while len(v2_split) < max_range:
            v2_split.append(0)
        print(v1_split)
        print(v2_split)
        for v1, v2 in zip(v1_split, v2_split):
            v1, v2 = int(v1), int(v2)
            print( v1 == v2,  v1 < v2,  v1> v2)
            if v1 == v2:
                continue
            elif v1 < v2:
                return -1
            else:
                return 1
        return 0