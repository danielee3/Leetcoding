/*
March Leetcoding Challenge Day 3
413. Arithmetic Slices
[Solution]
Language: C++
Time Complexity: O(n)
Space Complexity: O(1)
*/
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) return 0;
        int ans = 0;
        int diff = nums[1]-nums[0];
        int seq = 1;
        for (int i = 1; i < nums.size(); i++) {
            int newDiff = nums[i] - nums[i-1];
            if (diff == newDiff) seq++;
            else if (seq > 2) {
                ans += (seq - 2) * (seq - 1) / 2;
                seq = 2;
            }
            diff = newDiff;
        }
        if (seq > 2) ans += (seq - 2) * (seq - 1) / 2;
        return ans;
    }
};