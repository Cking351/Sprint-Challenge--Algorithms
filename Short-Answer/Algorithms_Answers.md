#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N) Linear/ As the input for the loop grows, so will the time it takes. It is Linear


b) O(n log n)Lineartithmic-ish/ The outer loop will scale as n grows. The inner loop will will scale faster than linear time as its input
increases.


c) O(N) Linear/ As n increases, the time it takes perform the recursive operation will scale proportionally

## Exercise II
I would use a binary search to find our target floor.
 - First we would take the total amount of floors and split them in half.
 - Check to see if the egg breaks at this mid point.
 - if the egg breaks, i would traverse down the lower floors until the floor where the egg does not break is found.
 - if the egg does not break, i would traverse up the higher floors until finding our target floor.

The time complexity for this at its worst would be O(logN) due to the use of the binary search and its
multiple iterations.