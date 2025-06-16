class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize a DP array of size n+1 with zeros to store the number of unique BSTs for each number of nodes
        # Base case: For 0 nodes (empty tree), there is 1 possible tree (the empty tree)
        # Base case: For 1 node, there is 1 possible tree (a single node)
        dp = {0: 1, 1: 1}
        
        # Iterate from 1 to n-1 to compute the number of unique BSTs for each number of nodes up to n
        # note that t means t+1 nodes in the tree
        for t in range(1, n):
            # Initialize a variable to store the total number of unique BSTs for t+1 nodes
            num = 0
            
            # Iterate over all possible root nodes (from 0 to t) to calculate the number of trees
            for i in range(t + 1):
                # For each root i, the number of trees is the product of:
                # - Number of trees possible with i nodes in the left subtree (dp[i])
                # - Number of trees possible with (t-i) nodes in the right subtree (dp[t-i])
                # to find totol combinations we need to multiply
                num += dp[i] * dp[t - i]
            
            # Store the computed number of unique BSTs for t+1 nodes in the DP array
            dp[t + 1] = num
        
        # Return the number of unique BSTs possible with n nodes
        return dp[n]