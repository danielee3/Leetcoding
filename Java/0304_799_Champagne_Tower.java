/*
March Leetcoding Challenge Day 4
799. Champagne Tower
[Solution]
Language: Java
Time Complexity: O(n^2)
Space Complexity: O(n^2)
where n is query_row
*/
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        if (poured == 0) return 0.0;
        double[][] glasses = new double[query_row+1][query_row+1];
        glasses[0][0] = poured;
        for (int r = 1; r <= query_row; r++) {
            int left = (int)Math.max(0, query_glass-query_row+r);
            for (int c = left; c <= query_glass; c++){
                if (c > 0 && glasses[r-1][c-1] > 1) {
                    glasses[r][c] += (glasses[r-1][c-1] - 1) / 2.0;
                }
                if (c < r && glasses[r-1][c] > 1) {
                    glasses[r][c] += (glasses[r-1][c] - 1) / 2.0;
                }
            }
        }
        return glasses[query_row][query_glass]>1?1:glasses[query_row][query_glass];
    }
}