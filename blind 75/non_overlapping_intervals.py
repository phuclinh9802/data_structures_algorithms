def non_overlap(intervals):
    intervals.sort()
    
    res = 0
    prevEnd = intervals[0]
    
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(prevEnd, end)
            
    return res