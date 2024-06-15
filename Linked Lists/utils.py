class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse(head: ListNode) -> None:
    temp = head
    while temp:
        if temp.next:
            print(f"{temp.val}->", end = "")
        else:
            print(f"{temp.val}")
        temp = temp.next