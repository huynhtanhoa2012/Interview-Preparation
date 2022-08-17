import heapq


def minMeetingRooms(intervals: list[list[int]]) -> int:

    if not intervals:
        return 0

    # Sort the given meeting by start time
    intervals.sort(key=lambda x:x[0])

    # Create min-heap
    free_rooms = []

    # Add first meeting ending time
    heapq.heappush(free_rooms, intervals[0][1])
    
    # For all the remaining meeting rooms
    for i in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)