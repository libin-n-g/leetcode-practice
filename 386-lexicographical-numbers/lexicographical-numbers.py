class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Initialize empty list to store result
        ret = []
        # Start with 1 as the first number
        num = 1
        # Continue until we have n numbers in result
        while len(ret) < n:
            # Add current number to result
            ret.append(num)
            # Check if multiplying by 10 is within bounds
            if num * 10 <= n:
                # Move to next level (e.g., 1 -> 10, 10 -> 100) 
                # going down the trie
                num *= 10
            else:
                # once reached highest level we increment by 1 
                # if num is already last node in level or reached n, then go up a level
                # Handle cases where we can't multiply by 10
                # If number ends in 9 or we've reached n
                while num % 10 == 9 or num == n:
                    # Move up one level (e.g., 19 -> 1, 29 -> 2)
                    # We get the node from which the prevous node was from. 
                    # Note that the increment from next line couses it to select next node. 
                    num //= 10
                # Increment to next number at current level
                num += 1
        # Return the lexicographically ordered list
        return ret

        # ret = []
        # def traverse_node(prev):
        #     ret = []
        #     value = prev*10
        #     if 0 < value <= n:
        #         ret.append(value)
        #         ret = ret + traverse_node(value)
        #     for num in range(1, 10):
        #         value = prev*10 + num
        #         # print(value)
        #         if value <= n:
        #             ret.append(value)
        #         else:
        #             break
        #         ret = ret + traverse_node(value)
        #     return ret 
        # return traverse_node(0)