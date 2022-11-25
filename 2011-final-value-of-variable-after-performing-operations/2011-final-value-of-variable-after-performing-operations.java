class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for (int i = 0; i < operations.length; i++) {
            if (operations[i].charAt(0)=='+' || operations[i].charAt(operations[i].length()-1)=='+') x++;
            else x--;
        }
        return x;
    }
}