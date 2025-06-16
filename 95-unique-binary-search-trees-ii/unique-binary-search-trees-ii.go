/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Memory struct {
    mem map[string][]*TreeNode
}

func (m *Memory) generateTrees(start, end int) []*TreeNode {
    var res []*TreeNode = make([]*TreeNode, 0)
    if start > end {
        res = append(res, nil)
    }
    var key string = fmt.Sprintf("%d, %d", start, end)
    if value, ok := m.mem[key]; ok {
        return value
    }
    for i := start; i <= end ; i++ {
        leftSubTrees := m.generateTrees(start, i-1)
        rightSubTrees := m.generateTrees(i+1, end)
        for _, left := range leftSubTrees {
            for _, right := range rightSubTrees {
                root := TreeNode{
                    Val: i,
                    Left: left,
                    Right: right,
                }
                res = append(res, &root)
            }
        }
    }
    m.mem[key] = res
    return res
}
func generateTrees(n int) []*TreeNode {
    m := &Memory {mem: make(map[string][]*TreeNode)}
    return m.generateTrees(1, n)
}