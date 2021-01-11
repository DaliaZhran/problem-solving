# https://leetcode.com/problems/course-schedule-iii/


# Priority Queue
# Time : O(nlogn)
# Space : O(n)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time = 0
        heap = []
        for t, d in courses:
            time += t
            heappush(heap, -t)
            if time > d:
                time += heappop(heap)

        return len(heap)
