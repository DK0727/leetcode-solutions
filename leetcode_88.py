class Solution:                         #第一种方法，遍历两个列表，取前面要求个数的数字最后排序
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result=[]
        for i in range(0,m):            #取num1中前m个数字，存储到result
            result.append(nums1[i])
        for j in range(0,n):            #取num2中前n个数字，存储到result
            result.append(nums2[j])
        for k in range(0,len(result)):  #把result里的数字改到num1（因为题目num1的列表长度=m+n，所以没出bug）
            nums1[k]=result[k]
        nums1.sort()                    #从小到大排序



class Solution:                         #第二种方法，因为m+n=len(num1),所以直接改
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,n):
            nums1[m+i]=nums2[i]
        nums1.sort()

class Solution:                         #第三种方法，双指针，比大小，从后往前
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k=m-1,n-1,m+n-1
        while i >= 0 and j >= 0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i -=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k -= 1
        while j >= 0:
            nums1[k]=nums2[j]
            j-=1
            k-=1







