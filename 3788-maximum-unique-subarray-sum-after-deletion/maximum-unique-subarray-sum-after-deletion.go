
func maxSum(nums []int) int {
    var maxValue int = 0
    counter := make(map[int]int)
    for i, e := range nums {
        counter[e]++
        if i==0 || e > maxValue {
            maxValue = e
        }
    }
    if maxValue <= 0 {
        return maxValue
    } else {
        total := 0
        for num := range(counter){
            if num > 0 {
                total += num
            }
        }
        return total
    }
}