# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        arrMap = [[-1 for _ in range(n)] for _ in range(m)]
        k = 0 # horizontal
        l = 0 # vertical

        a = 0
        b = 0

        verticalInterval = 0 # UP: 1 | DOWN: -1  
        horizontalInterval = 1 # RIGHT: 1 | LEFT: -1

        curr = head
        while (curr):
            # print(f"Condition: a: {a}, b: {b}, hI: {horizontalInterval}, vI: {verticalInterval}")
            arrMap[a][b] = curr.val

            if (horizontalInterval == 1 and b == n - 1):
                verticalInterval = 1 
                horizontalInterval = 0
                l += 1 # Top Wall

            elif (horizontalInterval == -1 and b == k):
                verticalInterval = -1
                horizontalInterval = 0
                m -= 1 # Bottom Wall

            elif (verticalInterval == 1 and a == m-1):
                verticalInterval = 0
                horizontalInterval = -1
                n -= 1 # Right Wall

            elif (verticalInterval == -1 and a == l):
                verticalInterval = 0
                horizontalInterval = 1
                k += 1 # Left Wall
            
            a += verticalInterval
            b += horizontalInterval

            curr = curr.next

        return arrMap