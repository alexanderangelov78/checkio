
def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """

    outputL = []
    inpL = []
    for item in intervals:
        inpL.append(list(item))

    # obhojdane na tuplite

    tempEl = [-1, -1]  #  active or last  interval
    for i in range(0, len(inpL)):

        # case 1 intervals has no common elements
        if tempEl[1] != -1 and ((tempEl[1] + 1) < inpL[i][0]):
            # update of outputList
            outputL.append(inpL[i])
            # tempEl accepts current interval tuple
            tempEl[0] = inpL[i][0]
            tempEl[1] = inpL[i][1]
        # overlaping end of previous and start of current interval
        # end of tempEl(previous interval) is => from start of current interval, or
        # end of tempEl(previous interval) is with 1  < from start of current interval and
        # end of current interval is greater than tempEl[1](end of active interval)
        elif tempEl[1] != -1 and (((tempEl[1] + 1) == inpL[i][0]) or (tempEl[1] >= inpL[i][0] and tempEl[1] < inpL[i][1])):
            pass
            tempEl[1] = inpL[i][1]
            outputL.pop()
            outputL.append([tempEl[0], tempEl[1]])
        # current interval is in active interval
        elif tempEl[1] != -1 and (inpL[i][1] <= tempEl[1]):
            pass
        elif tempEl[1] == -1:
            tempEl[0] = inpL[i][0]
            tempEl[1] = inpL[i][1]
            outputL.append(inpL[i])
    outL = []
    for el in outputL:
        outL.append(tuple(el))

    return iter(outL)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #res = merge_intervals(iter([(1, 13), (15, 16), (17, 20), (21, 22), (44, 74)]))
    res = merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(merge_intervals(iter([(1, 4), (2, 6), (8, 10), (12, 19)]))) == [
                                      (1, 6), (8, 10), (12, 19)], "First"
    assert list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [
                                      (1, 12)], "Second"
    assert list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [
                                      (1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')