def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        leftIdx = 0
        rightIdx = 0

        newArr = []

        while(leftIdx < m and rightIdx < n):
            if nums1[leftIdx] < nums2[rightIdx]:
                newArr.append(nums1[leftIdx])
                leftIdx += 1
            else:
                newArr.append(nums2[rightIdx])
                rightIdx += 1
        
        while(leftIdx < m):
            newArr.append(nums1[leftIdx])
            leftIdx += 1

        while(rightIdx < n):
            newArr.append(nums2[rightIdx])
            rightIdx += 1
        
        nums1 = newArr
        print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)