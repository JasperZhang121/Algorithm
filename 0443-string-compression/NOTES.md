### Two pointers
​
- The for loop traverses the list of characters from the second character to the last character. For each character, we check if it is the same as the previous character. If it is, we increment the count. If it is different, we write the previous character and its count to the list using the ptr pointer to keep track of the current position.
​
- If the count is greater than 1, we convert it to a string and write it to the list after the previous character. We update the ptr pointer to the end of the string.
​
- Finally, we return ptr, which represents the length of the compressed list.