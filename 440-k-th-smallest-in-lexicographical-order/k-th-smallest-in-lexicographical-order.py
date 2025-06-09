class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calculate_elements(base_node):
            result = 0
            neighbour_node = base_node + 1
            while base_node <= n:
                result += min(neighbour_node, n+1) - base_node
                # go to next level 
                base_node *=10
                neighbour_node *= 10
            return result
        current = 1
        num_elements_covered = 1
        while num_elements_covered < k:
            # caculate steps in the branch. 
            steps = calculate_elements(current)
            if num_elements_covered + steps <= k:
                # go to next branch
                current += 1
                num_elements_covered += steps
            else:
                # go down the branch. 
                current *= 10
                num_elements_covered += 1
        return current


