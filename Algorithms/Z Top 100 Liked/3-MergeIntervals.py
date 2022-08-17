def merge(intervals: list[list[int]]) -> list[list[int]]:
    # Sort invervals by the start
    intervals.sort(key = lambda i : i[0])

    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if lastEnd >= end:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append(start, end)
    return output