class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        # Initialize two pointers, start and end, and a hashtable to store the frequency of characters in s1
        start, end, table = 0, 0, [0] * 26
        for c in s1:
            table[ord(c) - ord('a')] += 1

        # Initialize a variable to store the number of characters that match the frequency in s1
        match = len(s1)

        # Iterate through s2 using the end pointer
        for end in range(len(s2)):
            # If the current character exists in s1, decrement the frequency in the hashtable
            if table[ord(s2[end]) - ord('a')] > 0:
                match -= 1

            # Decrement the frequency of the current character in the hashtable, even if it doesn't exist in s1
            table[ord(s2[end]) - ord('a')] -= 1

            # If the number of characters that match the frequency in s1 is 0, return True
            if match == 0:
                return True

            # If the end pointer minus the start pointer is equal to the length of s1, increment the start pointer
            if end - start + 1 == len(s1):
                # If the character at the start pointer exists in s1, increment the frequency in the hashtable
                if table[ord(s2[start]) - ord('a')] >= 0:
                    match += 1

                # Increment the frequency of the character at the start pointer in the hashtable
                table[ord(s2[start]) - ord('a')] += 1

                # Increment the start pointer
                start += 1

        # Return False if no permutation of s1 exists in s2
        return False
