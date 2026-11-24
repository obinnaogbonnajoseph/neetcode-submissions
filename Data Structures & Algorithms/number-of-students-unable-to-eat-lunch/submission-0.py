class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = n = len(students)
        idx = 0

        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and sandwich != students[idx]:
                idx = (idx + 1) % n
                cnt += 1
            if sandwich == students[idx]:
                students[idx] = -1
                res -= 1
            else:
                break

        return res
