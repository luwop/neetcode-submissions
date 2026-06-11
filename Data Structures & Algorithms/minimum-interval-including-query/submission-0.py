class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        queries = sorted((queries[indx], indx) for indx in range(len(queries)))
        res = [-1] * len(queries)
        min_heap = []
        i = 0
        
        for value, indx in queries:
            # Track potential intervals for the current query
            while i < len(intervals) and intervals[i][0] <= value:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1

            # Remove invalid intervals for the current query
            while min_heap and min_heap[0][1] < value:
                heapq.heappop(min_heap)

            # If there is a valid interval, track it
            if min_heap:
                res[indx] = min_heap[0][0]

        return res