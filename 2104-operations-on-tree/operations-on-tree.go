type LockingTree struct {
    ancestors map[int][]int
    children  map[int][]int
    locked    map[int]int
}

func Constructor(parent []int) LockingTree {
    ancestors := make(map[int][]int)
    children := make(map[int][]int)
    locked := make(map[int]int)

    // Initialize maps for all nodes
    for node := 0; node < len(parent); node++ {
        ancestors[node] = []int{}
        children[node] = []int{}
    }

    // Populate ancestors
    for node := 0; node < len(parent); node++ {
        current := node
        for current != -1 {
            if parent[current] != -1 {
                ancestors[node] = append(ancestors[node], parent[current])
            }
            current = parent[current]
        }
    }

    // Populate children
    for node := 1; node < len(parent); node++ {
        parentNode := parent[node]
        if parentNode != -1 {
            children[parentNode] = append(children[parentNode], node)
        }
    }

    return LockingTree{
        children:  children,
        ancestors: ancestors,
        locked:    locked,
    }
}

func (this *LockingTree) Lock(num int, user int) bool {
    if _, ok := this.locked[num]; !ok {
        this.locked[num] = user
        return true
    }
    return false
}

func (this *LockingTree) Unlock(num int, user int) bool {
    if value, ok := this.locked[num]; ok && value == user {
        delete(this.locked, num)
        return true
    }
    return false
}

func (this *LockingTree) Upgrade(num int, user int) bool {
    // Check if node is unlocked
    if _, ok := this.locked[num]; ok {
        return false
    }

    // Check if any ancestor is locked
    for _, ancestor := range this.ancestors[num] {
        if _, ok := this.locked[ancestor]; ok {
            return false
        }
    }

    // Traverse descendants to count locked ones and collect them
    lockedDescendants := []int{}
    queue := []int{num} // Start with children, not num
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        if children, ok := this.children[node]; ok {
            for _, child := range children {
                if _, ok := this.locked[child]; ok {
                    lockedDescendants = append(lockedDescendants, child)
                }
                queue = append(queue, child)
            }
        }
    }

    // Check if exactly one descendant is locked
    if len(lockedDescendants) < 1 {
        return false
    }

    // Unlock the descendant and lock the current node
    for _, descendant := range lockedDescendants{
        delete(this.locked, descendant)
    }
    this.locked[num] = user
    return true
}