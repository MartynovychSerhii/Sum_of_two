# Sum_of_two
Requirements:
1. Programming language - Python3.
2. Code should be clean and structured.
3. The solution should be stored and presented with GitHub.
   
Problem:
Given an array of integers numbers and an integer target. Implement function
def sum_of_two(numbers: list, target: int) -> list to return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice. You can return the answer in any order.
(Optional) Estimate time complexity of your solution.

Example 1:
Input: numbers = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because numbers[0] + numbers[1] == 9, we return [0, 1].

Example 2:

Input: numbers = [3,2,4], target = 6

Output: [1,2]

Example 3:
Input: numbers = [3,3], target = 6

Output: [0,1]

Constraints:

● 2 <= len(numbers) <= 1000.

● -1000 <= numbers[i] <= 1000.

● -1000 <= target <= 1000.

● Only one valid answer exists.
