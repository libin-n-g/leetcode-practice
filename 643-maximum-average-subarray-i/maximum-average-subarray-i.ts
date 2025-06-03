
function findMaxAverage(nums: number[], k: number): number {
    let sum: number = 0;
    let max_sum : number = 0;
    for ( let i = 0; i < nums.length; i++) {
        let temp = 0;
        if (i < k) {
            sum += nums[i];
            max_sum = sum;
        } else {
            sum -= nums[i-k];
            sum += nums[i];
            if (sum > max_sum) {
                max_sum = sum;
            }
        }
    }
    return max_sum / k;
};