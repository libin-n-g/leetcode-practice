
func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
    var not_opened_but_visited map[int]bool = map[int]bool{}
    var ret int = 0
    for i := 0; i < len(initialBoxes); i++ {
        curr_box := initialBoxes[i]
        // initialBoxes = initialBoxes[1:]
        if status[curr_box] == 1{
            ret += candies[curr_box]
            for _, key := range keys[curr_box] {
                status[key] = 1
                if _, ok := not_opened_but_visited[key]; ok {
                    initialBoxes = append(initialBoxes, key)
                    delete(not_opened_but_visited, key)
                }
            }
            for _, box := range containedBoxes[curr_box] {
                fmt.Println(box)
                initialBoxes = append(initialBoxes, box)
            }
        } else {
            not_opened_but_visited[curr_box] = true
        }
    }

    return ret
}