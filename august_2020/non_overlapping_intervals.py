from typing import List


class Solution:
    """
    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    Example 1:

    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

    Example 2:

    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

    Example 3:

    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

    Note:

        You may assume the interval's end point is always bigger than its start point.
        Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        if len(intervals) < 2:
            return 0
        prev = intervals[0]
        count = 0
        for curr in intervals[1:]:
            if prev[1] <= curr[0]:
                prev = curr
            else:
                count += 1
        return count
