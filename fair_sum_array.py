'''
Topics
Companies
Hint
You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.'''

class Solution:
    def waysToMakeFair(self, nums) -> int:
        prefix_sum_even = [0]*(len(nums))
        prefix_sum_odd = [0]*(len(nums))
        prefix_sum_even[0] = nums[0]
        ans = 0
        print(prefix_sum_even,  prefix_sum_odd)
        for i in range(1,len(nums)):
            if i%2==0:
                prefix_sum_even[i] = prefix_sum_even[i-1] + nums[i]
                prefix_sum_odd[i] = prefix_sum_odd[i-1]
            else:
                prefix_sum_odd[i] = prefix_sum_odd[i-1] + nums[i]
                prefix_sum_even[i] = prefix_sum_even[i-1]
        even_sum = 0
        odd_sum = 0
        for i in range(len(nums)):
            if i > 0:
                even_sum = prefix_sum_even[i-1] 
                odd_sum = prefix_sum_odd[i-1]
            even_sum = even_sum + (prefix_sum_odd[-1]-prefix_sum_odd[i])
            odd_sum = odd_sum + (prefix_sum_even[-1]-prefix_sum_even[i])
            if even_sum == odd_sum:  ans+=1
        return ans
        

s = Solution().waysToMakeFair([6,1,7,4,1])