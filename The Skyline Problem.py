# https://leetcode.com/problems/the-skyline-problem/


# Line sweep with heap
# Time: O(n log n)
# Space: O(2n)
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        positions = []
        for b in buildings:
            positions.append(b[0])
            positions.append(b[1])
        positions = sorted(set(positions))

        prev_h = 0
        ptr = 0  # buildings list iterator
        skyline = []
        alive = []
        for cur_pos in positions:
            # remove all buildings heights that ended from the heap
            while alive and alive[0][1] <= cur_pos:
                heappop(alive)

            # add all buildings that start at or before the cur pos
            while ptr < n and buildings[ptr][0] <= cur_pos:
                heappush(alive, [-buildings[ptr][2], buildings[ptr][1]])
                ptr += 1

            if alive:
                cur_h = -alive[0][0]
                if cur_h != prev_h:
                    skyline.append([cur_pos, cur_h])
                    prev_h = cur_h
            else:
                skyline.append([cur_pos, 0])

        return skyline


# Same Idea, different implementation -> faster
class Solution:
    import heapq

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos:
                heappop(live)
            if negH:
                heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]
