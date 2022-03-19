/*
March Leetcoding Challenge Day 18
316. Remove Duplicate Letters
[Solution]
Language: Java
Time Complexity: --
Space Complexity: --
*/
class Solution {
    public String removeDuplicateLetters(String s) {
        int last[] = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i)-'a'] = i;
        } 
             
        HashSet<Character> set = new HashSet<>(); 
        Stack<Character> stack = new Stack<>(); 
        int start = -1; 
        for (int i = 0; i < s.length(); i++) { 
            char c = s.charAt(i); 
            if (!set.contains(c)) { 
                while (!stack.empty() && stack.peek() > c && last[stack.peek()-'a']>i) {
                    set.remove(stack.pop());
                    
                } 
                set.add(c); 
                stack.push(c); 
            } 
        } 
        StringBuilder sb = new StringBuilder(); 
        while (!stack.empty()) {
            sb.append(stack.pop());
        } 
        return sb.reverse().toString();
        
    }
}