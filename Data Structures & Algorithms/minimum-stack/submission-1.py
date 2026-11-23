class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min -= pop

    def top(self) -> int | float:
        val = self.stack[-1]
        if val < 0:
            return self.min
        return self.min + val

    def getMin(self) -> int | float:
        return self.min
