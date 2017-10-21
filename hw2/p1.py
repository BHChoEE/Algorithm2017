def main():
    number = int(input())
    caseAns = []
    for i in range(number):
        inputNum = int(input())
        digit = [9, 8, 7, 6, 5, 4, 3, 2]
        factor = []
        ## factorization
        inputPrev = inputNum
        failed = False
        while inputNum != 1:
            for i in digit:
                if inputNum % i == 0:
                    factor.append(i)
                    inputNum /= i
            if inputPrev == inputNum:
                failed = True
                break
        if not failed:
            while len(factor) < 2:
                factor.append(1)
            factor.sort()
            outStr = ""
            for i in factor:
                outStr += str(i)
            caseAns.append(outStr)
        else:
            caseAns.append('input cannot be factorized to digits, the rest part is ' + str(inputNum))
    print ('')
    for i in caseAns:
        print(i)

if __name__ == '__main__':
    main()
