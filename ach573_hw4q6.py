#hw4q6

def appearances(s, low, high):
    thisdict = {}
    if low == high:
        thisdict[s[low]] = 1
    else:
        thisdict.update(appearances(s,low+1,high))
        if s[low] in thisdict:
            thisdict[s[low]] = thisdict[s[low]] + 1
        else:
            thisdict[s[low]] = 1
    return thisdict 

