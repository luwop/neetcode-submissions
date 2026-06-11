class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Suppose we have intervals i and j
        Case 1: i[0] < j[0]
        Case 2: i[1] < j[1] 
        """
        res = []

        for i, currInterval in enumerate(intervals):
            if currInterval[1] < newInterval[0]:
                res.append(currInterval)
            elif currInterval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], currInterval[0])
                newInterval[1] = max(newInterval[1], currInterval[1])

        res.append(newInterval)
        return res