class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=0
        l=len(nums)
        while n < l:
            if nums[n] == val:
                 nums[n]=nums[l-1]
                 l-=1
            else:
                n+=1
        return n

