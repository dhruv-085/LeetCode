class Solution:

    def last_occurance(self, nums: List[int], x: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = 0
        idx = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= x:
                ans = nums[mid]
                idx = mid
                low = mid + 1
            else:
                high = mid - 1

        return idx if ans == x else -1

    def first_occurance(self, nums: List[int], x: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = 0
        idx = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= x:
                ans = nums[mid]
                idx = mid
                high = mid - 1
            else:
                low = mid + 1

        return idx if ans == x else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        answer = []
        answer.append(self.first_occurance(nums, target))
        answer.append(self.last_occurance(nums, target))

        return answer