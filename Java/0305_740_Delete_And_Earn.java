/*
March Leetcoding Challenge Day 5
740. Delete and Earn
[Solution]
Language: Java
Time Complexity: O(n log n)
Space Complexity: O(n)
*/
class Solution {
    public int deleteAndEarn(int[] nums) {
        if (nums.length == 1) return nums[0];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num:nums) {
            map.put(num, map.getOrDefault(num, 0) + num);
        }
        Integer[] keyArr = map.keySet().toArray(Integer[]::new);
        Arrays.sort(keyArr);
        int[] dp = new int[keyArr.length+2];
        dp[2] = map.get(keyArr[0]);
        for (int i = 1; i < keyArr.length; i++) {
            if (keyArr[i] - 1 > keyArr[i-1]) dp[i+2] = Math.max(dp[i+1], dp[i]) + map.get(keyArr[i]);
            else dp[i+2] = Math.max(dp[i], dp[i-1]) + map.get(keyArr[i]);
        }
        return (int)Math.max(dp[dp.length-1], dp[dp.length-2]);
    }
}