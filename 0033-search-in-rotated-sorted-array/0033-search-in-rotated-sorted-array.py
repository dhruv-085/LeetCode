class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            ## First check if sorted from low to mid then proceed
            # i.e. left side
            if nums[low] <= nums[mid]:
                # if yes check whether lies on the left or not
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                
                ## not sorted now we have to check on which side to move by checking the target and the low value ofcourse
            # right side
            else:
                ## if I am on right side why would I compare left with mid, compare mid target and high to find search
                if nums[mid] <= target <= nums[high]:
                    ## because it exists on the right move low towards right 
                    low = mid + 1
                else:
                    high = mid - 1

        return -1