class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        if len(nums) < k:
            self.largestArr = sorted(nums)

            while len(self.largestArr) < k:
                self.largestArr.insert(0, -99999)
        else:
            self.largestArr = sorted(nums)[-k:]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        if val < self.largestArr[0]:
            return self.largestArr[0]
        
        for idx in range(len(self.largestArr)):
            if val < self.largestArr[idx]:
                self.largestArr.insert(idx, val)
                self.largestArr = self.largestArr[1:]
                return self.largestArr[0]

        self.largestArr.append(val)
        self.largestArr = self.largestArr[1:]
        return self.largestArr[0]

kl = KthLargest(1, [])
print(kl.add(3))
print(kl.add(5))
print(kl.add(10))
print(kl.add(9))
print(kl.add(4))
print(kl.largestArr)

