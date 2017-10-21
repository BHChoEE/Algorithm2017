import sys
########################################
# You can add supporting functions here





########################################
def match(men, women, mprefer, wprefer):
    ### TODO ###
    # Implement the Gale-Shapley algorithm.
    # You should return a dictionary of pairing result, use woman as key and man as
    # value.

    ## set all people status to free
    menStat = [0 for col in range(len(men))]
    menProp = [0 for col in range(len(men))]
    womenStat = [0 for col in range(len(women))]
    wives = {}
    while menStat != [1 for col in range(len(men))]:
        ## run through all men not engaged
        for m, man in enumerate(menStat):
            if man == 0:
                w = mprefer[m][menProp[m]]
                #print(w)
                menProp[m] += 1
                if womenStat[w] == 0:
                    wives[w] = m
                    menStat[m] = 1
                    womenStat[w] = 1
                    #print(wives)
                    break
                else:
                    mPrev = wives[w]
                    if women[w][m] < women[w][mPrev]:
                        wives[w] = m
                        menStat[m] = 1
                        menStat[mPrev] = 0
                        #print(wives)
                        break               
    return wives


def is_stable(men, women, mprefer, wives):
    if wives is None:
        wives = wives
    for w, m in wives.items():
        i = men[m][w]
        preferred = mprefer[m][:i]
        for p in preferred:
            h = wives[p]
            if women[p][m] < women[p][h]:  
                return False
    return True

if __name__ == '__main__':
    '''
    A reminder of the definitions of variables

    men is a 2D-list which presents men's rankings for women. 
    men[m][w]=i means man 'm' ranks woman 'w' as i.
    Note that every list is zero-based and 0 means the highest preference.
    For example, if there are 10 pairs of men and women, 
    they are denoted as m0, m1, ..., m9 and w0, w1, ..., w9
    men[1][2] = 0 means m1 likes w2 the most among all women.
    Similarly, women[1][2] = 1 means, for w1, m2 is her second choice.
    
    mprefer is a 2D-list which presents men's preference.  
    mprefer[m][i]=w means, for man 'm', his i-th preferable woman is 'w'
    For examples, mprefer[1][0]=2 means m1's first choice is w2.
    '''
    case = str(sys.argv[1])
    men = []
    men_file = 'men_' + case + '.txt'
    women_file = 'women_' + case + '.txt'
    for line in open(men_file, 'r'):
        man = list(map(int, line.split()))
        men.append(man)

    women = []
    for line in open(women_file, 'r'):
        woman = list(map(int, line.split()))
        women.append(woman)

    wives = {}
    pairs = []
    
    mprefer = []
    wprefer = []
    pair_num = len(men[0])
    
    for i in range(pair_num):
        mp = []
        wp = []
        for j in range(pair_num):
            mp.append(men[i][:].index(j))
            wp.append(women[i][:].index(j))
        mprefer.append(mp)
        wprefer.append(wp)
    
    wives = match(men, women, mprefer, wprefer)
    if is_stable(men, women, mprefer, wives):
        print('The matching is stable.')
    else:
        print('The matching is failed.')







