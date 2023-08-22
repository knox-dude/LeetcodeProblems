# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # get numbers out of linked list into arrays (still backwards)
        num1 = []
        num2 = []
        while l1.next != None:
            num1.append(l1.val)
            l1 = l1.next
        num1.append(l1.val)
        while l2.next != None:
            num2.append(l2.val)
            l2 = l2.next
        num2.append(l2.val)
        
        #make sure they are the same length by appending zeroes
        diff = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            for i in range(diff):
                num2.append(0)
        else:
            for i in range(diff):
                num1.append(0)
        
        #Start adding the two lists together
        finalNum = 0
        for i in range(len(num1)-1, -1, -1):
            firstToAdd = num1[i] * 10**i
            secondToAdd = num2[i] * 10**i
            finalNum = finalNum + firstToAdd + secondToAdd
        finalNum = str(finalNum)
        print(finalNum)
        
        #Form linked list to return
        headNode = ListNode()
        firstNode = ListNode()
        secondNode = ListNode()
        firstRun = True
        for i in range(len(finalNum)-1, -1, -1):
            result = int(finalNum[i])
            if firstRun:
                firstNode = headNode
                firstRun = False
            else:
                firstNode = secondNode
                secondNode = ListNode()
            firstNode.val = result
            if i != 0:
                firstNode.next = secondNode
        return headNode
