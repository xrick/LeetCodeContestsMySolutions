def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        retList = []
        for idx in range(left,right+1):
            intStr = str(idx)
            print("current intStr is : ",intStr)
            isSelfDivide = True
            for jdx in intStr:
                print("jdx is : ",jdx)
                tmp = int(jdx)
                if tmp == 0 or idx%tmp != 0:
                    isSelfDivide = False
                    continue
            if isSelfDivide :
                retList.append(idx)
        return retList


if __name__ == '__main__':
    res = selfDividingNumbers(1,22)
    if(res):
        print(res)
    else:
        print("null")

