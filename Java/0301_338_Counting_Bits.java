/*
March Leetcoding Challenge Day 1
338. Counting Bits
[Solution]
Language: Java
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n). 
*/
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];
        if (n == 0) return ans;
        ans[1] = 1;
        int big = 2;
        int count = big;
        for (int i = 2; i <= n; i++) {
            if (count == 0) {
                big *= 2;
                count = big;
            }
            ans[i] = ans[i-big] + 1;
            count--;
        }
        return ans;
    }
}