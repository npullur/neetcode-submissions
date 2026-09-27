class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # will use two pointers here
        # we will traverse from left increase, right decrease
        # when current sum greater than target, right decrease
        # when current sum less than target, left increase
        # if current sume eqauls, add +1 to index and store in list
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l+1, r+1]