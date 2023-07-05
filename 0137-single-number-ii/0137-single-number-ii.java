class Solution {
    public int singleNumber(int[] nums) {
        
        // Initialize seenOnce and seenTwice to 0
        int seenOnce = 0, seenTwice = 0;

        // Iterate through nums
        for (int num : nums) {
            // Update using derived equations
            seenOnce = (seenOnce ^ num) & (~seenTwice);
            seenTwice = (seenTwice ^ num) & (~seenOnce);
        }

        // Return integer which appears exactly once
        return seenOnce;
    }
}