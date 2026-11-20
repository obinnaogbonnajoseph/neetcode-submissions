class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        special_ops = ("+", "C", "D")
        for op in operations:
            if op not in special_ops:
                record.append(int(op))
            elif op == "+" and record[-1] and record[-2]:
                record.append(sum([record[-1], record[-2]]))
            elif op == "C":
                record.pop()
            elif op == "D" and record[-1]:
                record.append(record[-1] * 2)
        return sum(record)
