/*
March Leetcoding Challenge Day 25
1029. Two City Scheduling
[Solution]
Language: Java
Time Complexity: O(n log n)
Space Complexity: O(1)
*/
class Solution {
    public int twoCitySchedCost(int[][] costs) {
        int sum = 0;
        Comparator<int[]> comp = new Comparator<>(){
            public int compare (int[] a, int[] b) {
                return (a[1]-a[0]) - (b[1]-b[0]);
            }
        };
        // Comparator<int[]> comp = (a, b) -> (a[1]-a[0]) - (b[1]-b[0]);
        Arrays.sort(costs, comp);
        for (int i = 0; i < costs.length; i++) {
            if (i < costs.length / 2) {
                sum += costs[i][1];
            } else {
                sum += costs[i][0];
            }
        }
        return sum;
    }
}