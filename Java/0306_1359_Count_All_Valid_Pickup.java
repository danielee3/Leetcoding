/*
March Leetcoding Challenge Day 6
1359. Count All Valid Pickup and Delivery Options
[Solution]
Language: Java
Time Complexity: O(n)
Space Complexity: O(1)
*/
class Solution {
    public int countOrders(int n) {
        long ans = 1;
        for (int i = 1; i <= n; i++) {
            ans *= i;
            ans *= (2*i-1);
            ans %= 1000000007;
        }
        return (int)ans;   
    }
}