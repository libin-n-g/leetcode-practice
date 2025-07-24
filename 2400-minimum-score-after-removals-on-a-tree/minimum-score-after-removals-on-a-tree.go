func minimumScore(nums []int, edges [][]int) int {
    N := len(nums)

	// Create adjacency list representation of the tree
	edgesMap := make(map[int][]int)
	for _, edge := range edges {
		s, e := edge[0], edge[1]
		edgesMap[s] = append(edgesMap[s], e)
		edgesMap[e] = append(edgesMap[e], s)
	}

	// Array to store XOR sum of each subtree
	xorSumTree := make([]int, N)

	// DFS to calculate XOR sum of each subtree
	var calculateXorSum func(node, parent int) int
	calculateXorSum = func(node, parent int) int {
		currentSum := nums[node]
		for _, t := range edgesMap[node] {
			if t != parent {
				currentSum ^= calculateXorSum(t, node)
			}
		}
		xorSumTree[node] = currentSum
		return currentSum
	}
	calculateXorSum(0, -1)

	// Array to store set of nodes in each subtree
	treeNodes := make([]map[int]bool, N)
	for i := range treeNodes {
		treeNodes[i] = make(map[int]bool)
	}

	// DFS to build sets of nodes for each subtree
	var addTreeNodes func(node, parent int) map[int]bool
	addTreeNodes = func(node, parent int) map[int]bool {
		treeNodes[node][node] = true
		for _, t := range edgesMap[node] {
			if t != parent {
				childNodes := addTreeNodes(t, node)
				for child := range childNodes {
					treeNodes[node][child] = true
				}
			}
		}
		return treeNodes[node]
	}
	addTreeNodes(0, 0)

	// Initialize best score as infinity
	best := math.MaxInt32

	// Helper function to check if node x is in subtree of y
	hasNode := func(x int, yNodes map[int]bool) bool {
		return yNodes[x]
	}

	// Try all possible pairs of edges to remove
	for i := 1; i < N; i++ {
		for j := i + 1; j < N; j++ {
			var treeO, treeI, treeJ int
			// Case 1: If node i is in subtree of j
			if hasNode(i, treeNodes[j]) {
				treeO = xorSumTree[0] ^ xorSumTree[j]
				treeI = xorSumTree[i]
				treeJ = xorSumTree[j] ^ xorSumTree[i]
			// Case 2: If node j is in subtree of i
			} else if hasNode(j, treeNodes[i]) {
				treeO = xorSumTree[0] ^ xorSumTree[i]
				treeI = xorSumTree[i] ^ xorSumTree[j]
				treeJ = xorSumTree[j]
			// Case 3: If subtrees i and j are disjoint
			} else {
				treeO = xorSumTree[0] ^ xorSumTree[i] ^ xorSumTree[j]
				treeI = xorSumTree[i]
				treeJ = xorSumTree[j]
			}

			// Calculate score as max XOR - min XOR of the three components
			maxVal := max(treeO, max(treeI, treeJ))
			minVal := min(treeO, min(treeI, treeJ))
			best = min(best, maxVal-minVal)
		}
	}

	return best
}