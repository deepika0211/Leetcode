# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        a=[]
        if not head:
            return head
        temp=head
        k=head
        while temp:
            a.append(temp.val)
            temp=temp.next
        a=sorted(a)
        for i in a:
            k.val=i
            k=k.next
        return head
        