- Initialize an empty list to hold the answers and a SortedList to hold the values of the sliding window.
- Iterate through the input array and add each value to the SortedList.
- If the size of the SortedList is greater than k, remove the leftmost element from the
- SortedList to maintain the sliding window of size k.
- If the index is greater than or equal to k-1, find the xth smallest integer in the current subarray using the SortedList.
- Append the beauty of the current subarray to the answer list.
Return the answer list.