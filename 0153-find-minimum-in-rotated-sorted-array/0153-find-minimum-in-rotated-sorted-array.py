class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        min = float('inf')

        while low <= high:
            mid = (low + high) // 2

            ## Use the property of sorted array
            if nums[low] <= nums[mid]:
                ## Hey left are you sorted? 
                # Okay pick min and eleminate it, move towards right
                
                if nums[low] <= min: 
                    min = nums[low]
                
                low = mid + 1

            else:
                ## Right you are sorted pick min i.e. nums[mid] and eleminate right
                if nums[mid] <= min: 
                    min = nums[mid]

                high = mid - 1
        
        return min