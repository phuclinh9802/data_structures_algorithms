def insert_interval(intervals, newInterval):
    # we use brute force approach with some math conditions when overlapping

    res = [] # O(n) if not counted res as extra mem

    for i in range(len(invervals)):
        # 1. newInterval at beginning & not overlapping current interval
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:] # return newInterval + the rest of the intervals from i -> len(intervals)
        # 2. newInterval at the end & not overlapping
        if newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    res.append(newInterval)

    return res
