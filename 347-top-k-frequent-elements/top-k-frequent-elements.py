class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        top_values = [[] for _ in range(len(nums)+1)]
        for key, v in counter.items():
            top_values[v].append(key)
        ret = []
        for i in range(len(nums), -1, -1):
            ret += top_values[i]
            if len(ret) >= k:
                return ret
        return ret
        
        # def quickselect(arr, k):
        #     # print(arr, k)
        #     if len(arr) <= k:
        #         return arr
        #     pivot = arr[-1]
        #     left, right =set(), set()
        #     for num in arr:
        #         if num < pivot: 
        #             left.add(num)
        #         elif num > pivot:
        #             right.add(num)
        #     # print(left, pivot, right)
        #     if len(left) + 1 == k:
        #         left.add(pivot)
        #         return left
        #     elif len(left) >= k:
        #         return quickselect(list(left), k)
        #     else:
        #         left.add(pivot)
        #         left = left.union(quickselect(list(right), k - len(left)))
        #         return left
        # return list(quickselect(nums, k))