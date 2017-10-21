###################
## Util Function ##
###################
def transposeMatrix(m):
    t = []
    rowLen = len(m)
    colLen = len(m[0])
    for c in range(colLen):
        tRow = []
        for r in range(rowLen):
            tRow.append(m[r][c])
        t.append(tRow)
    return t

def getMatrixMinor(m, i , j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i+1:])]

def getMatrixDet(m):
    #base case for 2x2 matrix
    if len(m) == 2 and len(m[0]) == 2:
        return m[0][0] * m[1][1]- m[0][1] * m[1][0]

    det = 0
    for c in range(len(m)):
        det += ((-1)**c)*m[0][c]*getMatrixDet(getMatrixMinor(m,0,c))
    return det

def getMatrixInverse(m):
    det = float(getMatrixDet(m))
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [ [m[1][1] / det, -1*m[0][1] / det],
                 [-1*m[1][0] / det, m[0][0] / det] ]
    # general case
    invM = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append( ((-1) ** (r+c)) * float(getMatrixDet(minor)) )
        invM.append(cofactorRow)
    invM = transposeMatrix(invM)
    for r in range(len(invM)):
        for c in range(len(invM)):
            invM[r][c] = invM[r][c] / det
    return invM

def matrixMul(x, y):
    """Return product of an MxP matrix A with an PxN matrix B."""
    cols, rows = len(y[0]), len(y)
    resRows = xrange(len(x))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j in xrange(cols):
            for k in  xrange(rows):
                rMatrix[idx][j] += x[idx][k] * y[k][j]
    return rMatrix

def generateM(i, j, m):
    matrix = []
    for rowI in range(i - j + 1):
        row = []
        for colI in range(m+1):
            row.append( (rowI + 1 + j) ** colI)
        matrix.append(row)
    return matrix

def dotM(a, M):
    #if len(a) != len(M[0]):
    #    return []
    matrix = []
    for i in range(len(M)):
        dot = 0.0
        for j in range(len(M[0])):
            dot += M[i][j] * a[j][0]
        matrix.append(dot)
    return matrix
def getMinCost(y, approximation):
    se = 0.0
    #if len(y) != len(approximation):
    #    return -1
    #print "y: " 
    #print y[0]
    #print "approx: "
    #print approximation
    for i in range(len(y)):
        se += (y[i][0] - approximation[i]) ** 2
    return se

###################
## Main Function ##
###################      
def main():
    ## parser 
    str1 = str(raw_input())
    lastChar = 0
    params = []
    blank = True
    for i, char in enumerate(str1):
        if char == ' ' :
            if not blank:
                params.append(int(str1[lastChar:i]))
                lastChar = i + 1
            blank = True
        else:
            blank = False
        if len(str1) - 1 == i:
            if char != ' ':
                params.append(int(str1[lastChar:len(str1)]))
        if len(params) == 3:
            break
        
    n = params[0]
    m = params[1]
    C = params[2]
    y = []

    str2 = str(raw_input())
    lastChar2 = 0
    blank2 = True
    for i, char in enumerate(str2):
        if char == ' ' :
            if not blank2:
                y.append(int(str2[lastChar2:i]))
                lastChar2 = i + 1
            blank2 = True
        else:
            blank2 = False
        if len(str2) - 1 == i:
            if char != ' ':
                y.append(int(str2[lastChar2:len(str2)]))
        if len(y) == n:
            break
    Y = []
    Y.append(y)
    tranY = transposeMatrix(Y)
    '''
    ## constructing weight matrix A
    M = []
    for i in range(n):
        mi = []
        n = i + 1
        for j in range(m + 1):
            mi.append(pow(n, j))
        M.append(mi)
    transposeM = transposeMatrix(M)
    squareM = getMatrixInverse( matrixMul(transposeM, M ) )  
    '''
    ### costTable[] = dp table
    '''
    costTable[i][j] stands for min cost for y[i:j+1]
    costTable[i][j] can be split down to costTable[i][k+1] + costTable[k][j+1] + C
    '''
    ## intialize costTable 
    costTable = []
    for i in range(n):
        costRow = []
        for i in range(n):
            costRow.append(0.0)
        costTable.append(costRow)
    ## construct table bottom up
    for i in range(n):
        for j in range(i, -1, -1):
            ## diagonal is set to zero for costTable[i][i] must be fitted as zero
            if i == j:
                costTable[i][j] = 0.0
            else:
                ## calulate cost of costTable[i][j] itself
                matrixM = generateM(i, j, m)
                transposeM = transposeMatrix(matrixM)
                mulM = matrixMul(transposeM, matrixM)
                if  i - j + 1 <= m:
                    minCost = 0.0
                else:  
                    squareM = getMatrixInverse( matrixMul(transposeM, matrixM))
                    vecY = tranY[j:i+1]
                    #print(vecY)
                    matrixX = matrixMul(transposeM, vecY)
                    A = matrixMul(squareM, matrixX)
                    #print(A)
                    approx = dotM(A, matrixM)
                    #print (approx)
                    minCost = getMinCost(vecY, approx)
                
                ## calculate cost if break down to costTable[i][k+1] and costTable[k][j] + C
                for k in range(i - j):
                    cost1 = costTable[i][i - k]
                    cost2 = costTable[i - k - 1][j]
                    minCost = min(minCost, cost1 + cost2 + C)
                costTable[i][j] = minCost

    ## answer is costTable[n-1][0] for the whole string with len(n) and find round 
    
    ans = int(costTable[n-1][0])
    if float(ans + 1) - costTable[n-1][0] <= 0.5:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()