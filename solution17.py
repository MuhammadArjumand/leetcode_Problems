class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution(object):
    def deleteDuplicate(self,head):
        curr=head
        if (curr==None):
            return
        nxt=curr.next
        while(nxt!= None):
            if(curr.val==nxt.val):
                curr.next=nxt.next
                nxt=nxt.next
            else: 
                curr=curr.next
        return head

    





