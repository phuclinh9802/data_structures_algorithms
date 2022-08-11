def merge_interval(intervals):
    intervals.sort(key = lambda i:i[0])

    res = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = res[-1][1]

        if start <= lastEnd:
            res[-1][1] = max(end, lastEnd)

        else:
            res.append([start, end])

    return res