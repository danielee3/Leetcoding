/*
March Leetcoding Challenge Day 19
895. Maximum Frequency Stack
[Solution]
Language: Java
Time Complexity: --
Space Complexity: --
*/
class FreqStack {
    Map<Integer, Integer> freqMap;
    Map<Integer, Stack<Integer>> freqStack;
    int maxFreq;
    public FreqStack() {
        freqMap = new HashMap();
        freqStack = new HashMap();
        maxFreq = 0;
    }
    
    public void push(int val) {
        freqMap.put(val, freqMap.getOrDefault(val, 0) + 1);
        int freq = freqMap.get(val);
        Stack<Integer> stack;
        if (freqStack.containsKey(freq)){
            stack = freqStack.get(freq);
            if (stack.size() == 0) maxFreq++;
        } else {
            stack = new Stack();
            maxFreq++;
        }
        stack.push(val);
        freqStack.put(freq, stack);
    }
    
    public int pop() {
        int ans = freqStack.get(maxFreq).pop();
        System.out.println(ans);
        if (freqStack.get(maxFreq).empty()) maxFreq--;
        freqMap.put(ans, freqMap.get(ans)-1);
        return ans;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */