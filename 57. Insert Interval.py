intervals = [[3,5],[12,15]]
newInterval = [6,6]
sortedIntervals = []
inserted = False

if len(intervals) == 0:
    print(newInterval)

idx = 0
intervals.append([9999, 9999])

if newInterval[1] < intervals[0][0]:
    inserted = True
    sortedIntervals.append(newInterval)

while idx < len(intervals):
    print(f"Iteration: {idx}, Interval: {intervals[idx]}")
    if newInterval[0] > intervals[idx][0] or inserted:
        if idx != 0:
            print(f"\t\tInserting {intervals[idx-1]}")
            sortedIntervals.append(intervals[idx-1])
    elif (intervals[idx-1][1] < newInterval[0] ):
        print(f"\t[2] Interval previous: {intervals[idx-1]}")

        if intervals[idx][0] >= newInterval[0] and idx != len(intervals)-1 and newInterval[1] > intervals[idx][0]:
            # Berarti ada yang nabrak
            print("Nabrak")
            sortedIntervals.append(intervals[idx-1])
            idx += 1

            min_num = min(intervals[idx][0], newInterval[0])

            while newInterval[1] >= intervals[idx][0]:
                idx += 1 
            
            max_num = max(intervals[idx-1][1], newInterval[1]) 
            sortedIntervals.append([
                min_num,
                max_num
            ])
        else:
            sortedIntervals.append(intervals[idx-1])
            sortedIntervals.append(newInterval)

        inserted = True
    else:
        print(f"\tInterval previous: {intervals[idx-1][1]}, New Interval: {newInterval[0]}")
        createdIntv = [min(intervals[idx-1][0], newInterval[0])]

        while newInterval[1] >= intervals[idx][0]:
            idx += 1
        
        createdIntv.append(max(intervals[idx-1][1], newInterval[1]))
        sortedIntervals.append(createdIntv)
        print(f"\t\tInserting {createdIntv}")
        inserted = True

    idx += 1

print(sortedIntervals)