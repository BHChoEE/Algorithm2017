import time
import sys

########################################
# You can add supporting functions here
def mergesort(x, count):
    if len(x) > 1:
    ## Cut the list x into three part  
        if len(x) > 2:
            if len(x) % 3 == 0:       
                LeftCut = len(x) // 3 
                RightCut = LeftCut * 2
            elif len(x) % 3 == 1:
                LeftCut = len(x) // 3 + 1
                RightCut = 2 * (len(x) // 3) + 1
            elif len(x) % 3 == 2:
                LeftCut = len(x) // 3 + 1
                RightCut = 2 * (len(x) // 3) + 2
            LeftPart = x[:LeftCut]
            MidPart = x[LeftCut: RightCut ]
            RightPart = x[RightCut : ]
        else:
            LeftPart = [x[0]]
            MidPart = [x[1]]
            RightPart = []
    ## MergeSort
        (xl, lcount) = mergesort(LeftPart, 0)
        (xm, mcount) = mergesort(MidPart, 0)
        (xr, rcount) = mergesort(RightPart, 0)
        
    ## merge
        i = 0
        while len(xl) != 0 and len(xm) != 0 and len(xr) != 0:
            if xl[0] <= xm[0] and xl[0] <= xr[0]:
                x[i] = xl[0]
                xl.remove(xl[0])
            elif xm[0] <= xl[0] and xm[0] <= xr[0]:
                x[i] = xm[0]
                xm.remove(xm[0])
            else:
                x[i] = xr[0]
                xr.remove(xr[0])
            i += 1 
        while len(xl) != 0 and len(xm) != 0:
            if xl[0] < xm[0]:
                x[i] = xl[0]
                xl.remove(xl[0])
            else:
                x[i] = xm[0]
                xm.remove(xm[0])
            i += 1
        while len(xl) != 0 and len(xr) != 0:
            if xl[0] < xr[0]:
                x[i] = xl[0]
                xl.remove(xl[0])
            else:
                x[i] = xr[0]
                xr.remove(xr[0])
            i += 1
        while len(xm) != 0 and len(xr) != 0:
            if xm[0] < xr[0]:
                x[i] = xm[0]
                xm.remove(xm[0])
            else:
                x[i] = xr[0]
                xr.remove(xr[0])
            i += 1
        while len(xl) != 0:
            x[i] = xl[0]
            xl.remove(xl[0])
            i += 1
        while len(xm) != 0:
            x[i] = xm[0]
            xm.remove(xm[0])
            i += 1
        while len(xr) != 0:
            x[i] = xr[0]
            xr.remove(xr[0])
            i += 1
        return x, lcount + mcount + rcount + 1
    else:
        return x, 0
########################################
'''
def mergesort(x, count):
    ### TODO ###
    # Implement the merge sort algorithm.
    # x is a list with N elements.
    # You must return a sorted list and a counter of splitting number. 
    
    ## if list is cut to only two elements , go check the first element
    if len(x) == 2:
        if x[0] > x[1]:
            tmp = x[0]
            x[0] = x[1]
            x[1] = tmp
        count += 1

    elif len(x) > 2:
    ## Cut the list x into three part         
        LeftCut = len(x) // 3
        RightCut = LeftCut * 2
        LeftPart = x[:LeftCut]
        MidPart = x[LeftCut: RightCut]
        RightPart = x[RightCut: ]

    ## MergeSort
        (xl, lcount) = mergesort(LeftPart, 0)
        (xm, mcount) = mergesort(MidPart, 0)
        (xr, rcount) = mergesort(RightPart, 0)
        count = lcount + mcount + rcount + 1

    ## casewise condition
        l = 0
        m = 0
        r = 0
        i = 0

        while l < len(xl) and m < len(xm) and r < len(xr):
            if xl[l] <= xm[m] and xl[l] <= xr[r]:
                x[i] = xl[l]
                l += 1
            elif xm[m] <= xl[l] and xm[m] <= xr[r]:
                x[i] = xm[m]
                m += 1
            elif xr[r] <= xl[l] and xr[r] < xm[m]: 
                x[i] = xr[r]
                r += 1
            i += 1
        while l < len(xl) and m < len(xm):
            if xl[l] < xm[m]:
                x[i] = xl[l]
                l += 1
            else:
                x[i] = xm[m]
                m += 1
            i += 1
        while l < len(xl) and r < len(xr):
            if xl[l] < xr[r]:
                x[i] = xl[l]
                l += 1
            else:
                x[i] = xr[r]
                r += 1
            i += 1
        while m < len(xm) and r < len(xr):
            if xm[m] < xr[r]:
                x[i] = xm[m]
                m += 1
            else:
                x[i] = xr[r]
                r += 1
            i += 1
        while l < len(xl):
            x[i] = xl[l]
            l += 1
            i += 1
        while m < len(xm):
            x[i] = xm[m]
            m += 1
            i += 1
        while r < len(xr):
            x[i] = xr[r]
            r += 1
            i += 1
    return x, count
'''
if __name__ == '__main__':
    case = sys.argv[1]
    test_name = 'test_'+str(case)+'.txt'
    out_name = 'out_'+str(case)+'.txt'
    file_in = open(test_name, 'r')
    file_out = open(out_name, 'w')
    start_time = time.time()
    l = file_in.readline().split()
    l = list(map(int, l))
    count = 0 
    result, count = mergesort(l, count)
    #print(count)
    for i in result:
        file_out.write(str(i)+' ')
    file_out.write('\n')
    file_out.write(str(count))
    print('Timer: ', time.time()-start_time)
