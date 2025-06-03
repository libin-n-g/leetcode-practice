class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int l = 0;
        int r = nums.size() - 1;
        int operations = 0;
        int sum = 0;
        sort(nums.begin(), nums.end());
        while (l < r){
            sum = nums[l] + nums[r];
            if (sum == k){
                operations++;
                l++;
                r--;
            } else if (sum > k){
                r--;
            } else {
                l++;
            }
        }
        return operations;
    }
};