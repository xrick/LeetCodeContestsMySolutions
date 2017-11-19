def isOneBitCharacter(bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if(len(bits) == 1):
            if(bits[0] == 1):
                return False
            else:
                return True
        if(len(bits) == 2):
            if(bits[0] == 1):
                return False
            else:
                return True
        if(bits[0] == 0):
            return isOneBitCharacter(bits[1:])
        else:
            return isOneBitCharacter(bits[2:])

if __name__ == '__main__':
    res = isOneBitCharacter([1,1,1,1,0])
    if(res):
        if res == True :
            print("true")
        else:
            print("false")
    else:
        print("null")