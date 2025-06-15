class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen_count = set()
        for key in counter:
            if counter[key] in seen_count:
                return False
            seen_count.add(counter[key])
        return True