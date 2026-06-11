"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda x: x.start)

        rooms = []
        heapq.heappush(rooms, intervals[0].end)
        ct = 1

        for i in range(1, len(intervals)):
            # Free up rooms that have ended before this meeting starts
            while rooms and intervals[i].start >= rooms[0]:
                heapq.heappop(rooms)

            # Allocate new room
            heapq.heappush(rooms, intervals[i].end)
            ct = max(ct, len(rooms))

        return ct
