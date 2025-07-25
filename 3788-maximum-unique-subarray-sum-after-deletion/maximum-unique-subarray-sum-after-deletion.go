// import "fmt"
func maxSum(nums []int) int {
    var maxValue int = 0
    for i, e := range nums {
        if i==0 || e > maxValue {
            maxValue = e
        }
    }
    if maxValue <= 0 {
        return maxValue
    } else {
        total := 0
        counter := make(map[int]int)
        for _, num := range(nums){
            if num > 0 {
                if count, ok := counter[num]; !ok || count == 0 {
                    total += num
                    counter[num]++
                }
            }
        }
        return total
    }
}