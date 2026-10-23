class BrowserNode:
    def __init__(self, val: str, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = BrowserNode(homepage)

    def visit(self, url: str) -> None:
        node = BrowserNode(url, prev=self.cur)
        self.cur.next = node
        self.cur = node

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
