class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        hash_set = defaultdict(int)
        for student in students:
            hash_set[student] += 1

        for sandwich in sandwiches:
            if hash_set[sandwich] > 0:
                hash_set[sandwich] -= 1
                res -= 1
            else:
                break

        return res
