func countHillValley(nums []int) int {
    lastSignificantindex := 0
    count := 0
    for i := 1 ; i < len(nums)-1; i++ {
        if nums[i] == nums[i+1] {
            continue
        } else if nums[i] > nums[lastSignificantindex] && nums[i] > nums[i+1] {
            count++ // Hill
        } else if nums[i] < nums[lastSignificantindex] && nums[i] < nums[i+1] {
            count++ // Vally
        }
        lastSignificantindex = i
    }
    return count
}