
function findMaxAverage(nums: number[], k: number): number {
    let sum: number = 0;
    let max_average : number = 0;
    for ( let i = 0; i < nums.length; i++) {
        let temp = 0;
        if (i < k) {
            sum += nums[i];
            max_average = sum / k;
        } else {
            sum -= nums[i-k];
            sum += nums[i];
            temp = sum / k;
            if (temp > max_average) {
                max_average = temp;
            }
        }
    }
    return max_average;
};