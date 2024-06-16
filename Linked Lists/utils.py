class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_ll(arr: list[int]) -> ListNode:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    curr = head

    for i in range(1, len(arr)):
        num = ListNode(arr[i])
        curr.next = num
        curr = num
    
    return head

def ll_to_array(head: ListNode) -> list[int]:
    res = []
    temp = head

    while temp:
        res.append(temp.val)
        temp = temp.next
    
    return res

def traverse(head: ListNode) -> None:
    temp = head
    while temp:
        if temp.next:
            print(f"{temp.val}->", end = "")
        else:
            print(f"{temp.val}")
        temp = temp.next