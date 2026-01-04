# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        array=[]
        temp=head

        while temp and temp.next:
            array.append(temp.val)
            temp=temp.next.next
        if temp:
            array.append(temp.val)

        temp=head.next
        
        while temp and temp.next:
            array.append(temp.val)
            temp=temp.next.next
        if temp:
            array.append(temp.val)
        
        #reset temp
        temp=head
        i=0
        while temp:
            temp.val=array[i]
            temp=temp.next
            i+=1
        return head    