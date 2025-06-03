class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)
        visited = set()
        not_opened = set()
        ret = 0
        while queue:
            curr_node = queue.popleft()
            if status[curr_node] == 1:
                ret += candies[curr_node]
                for i in containedBoxes[curr_node]:
                    if i not in visited:
                        queue.append(i)
                for i in keys[curr_node]:
                    status[i] = 1
                    if i in not_opened:
                        queue.append(i)
                        not_opened.remove(i)
                visited.add(curr_node)
            else:
                not_opened.add(curr_node)
        return ret