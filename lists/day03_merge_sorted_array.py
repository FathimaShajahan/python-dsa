# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


# Function to create a linked list from a Python list
def createLinkedList(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Function to print linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


# ---------------- MAIN ----------------

# Input
list1 = [1,2,3]
list2 = [3,4,5,6]

# Create linked lists
head1 = createLinkedList(list1)
head2 = createLinkedList(list2)

# Merge
obj = Solution()
merged = obj.mergeTwoLists(head1, head2)

# Output
print("Merged Linked List:")
printLinkedList(merged)