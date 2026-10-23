class BrowserNode:
    def __init__(self, val: str, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = BrowserNode(homepage)
        self.cur_idx = 0

    def get(self, index: int) -> BrowserNode:
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def visit(self, url: str) -> None:
        tail = self.get(self.cur_idx)
        node = BrowserNode(url, prev=tail)
        tail.next = node
        self.cur_idx += 1

    def back(self, steps: int) -> str:
        cur = self.get(self.cur_idx)
        while cur.prev and steps > 0:
            cur = cur.prev
            steps -= 1
            self.cur_idx -= 1
        return cur.val

    def forward(self, steps: int) -> str:
        cur = self.get(self.cur_idx)
        while cur.next and steps > 0:
            cur = cur.next
            steps -= 1
            self.cur_idx += 1
        return cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
