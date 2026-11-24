class ListNode:
    def __init__(
        self, val: int = 0, next: Optional["ListNode"] = None, prev: Optional["ListNode"] = None
    ):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index: int) -> Optional[ListNode]:
        if index < 0 or index > self.size:
            return None
        if index < self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur
        else:
            cur = self.tail
            for _ in range(self.size - index + 1):
                cur = cur.prev
            return cur

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self.getPrev(index)
        next = prev.next
        node = ListNode(val, next, prev)
        prev.next = node
        next.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.getPrev(index)
        cur = prev.next
        next = cur.next
        prev.next = next
        next.prev = prev
        self.size -= 1
