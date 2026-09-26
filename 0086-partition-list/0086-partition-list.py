class Solution:
    def partition(self, head, x):
        before = ListNode(0)
        after = ListNode(0)

        before_curr = before
        after_curr = after

        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = before_curr.next
            else:
                after_curr.next = head
                after_curr = after_curr.next

            head = head.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next