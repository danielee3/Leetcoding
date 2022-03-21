/*
March Leetcoding Challenge Day 20
1007. Minimum Domino Rotations for Equal Row
[Solution]
Language: Java
Time Complexity: O(n)
Space Complexity: O(1)
*/
class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int cand1 = tops[0];
        int cand2 = bottoms[0];
        for (int i = 1; i < tops.length; i++) {
            if (tops[i] != cand1 && bottoms[i] != cand1) cand1 = -1;
            if (tops[i] != cand2 && bottoms[i] != cand2) cand2 = -1;
        }
        if (cand1 + cand2 < 0) return -1;
        int flips1 = 0;
        if (cand1 < 0) flips1 = Integer.MAX_VALUE;
        else {
            int topFlip = 0;
            int bottomFlip = 1;
            for (int i = 1; i < tops.length; i++) {
                int top = tops[i];
                int bottom = bottoms[i];
                if (top != cand1) topFlip++;
                if (bottom != cand1) bottomFlip++;
            }
            flips1 = Math.min(Math.min(topFlip, tops.length-topFlip), Math.min(bottomFlip, tops.length-bottomFlip));
            
        }
        int flips2 = 0;
        if (cand2 < 0) flips2 = Integer.MAX_VALUE;
        else {
           int topFlip = 1;
           int bottomFlip = 0;
           for (int i = 1; i < tops.length; i++) {
                int top = tops[i];
                int bottom = bottoms[i];
                if (top != cand2) topFlip++;
                if (bottom != cand2) bottomFlip++;
            }
            flips2 = Math.min(Math.min(topFlip, tops.length-topFlip), Math.min(bottomFlip, tops.length-bottomFlip));
        }
        
        
        return Math.min(flips1, flips2);
    }
}