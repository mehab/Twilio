def DESEBC(rounds,zeroString,bitKey,S1,S2,dictionary,reverse_slice):
    #region declaration
    binaryxor=''
    binaryRight=''
    finalEncryptedString=''
    #endregion
    i=0
    round=0
    while i<len(zeroString):
        pt=zeroString[i:i+12]
        i=i+12
        left=pt[:6]
        right=pt[6:]
        while round<rounds:
            print("Computing for round number:"+str(round))
            if(round<2):
                uKey=bitKey[round:round+8]
            else:
                uKey=bitKey[round:]+bitKey[0:(8-len(bitKey[round:]))] #round key generation
            eOfR=right[0:2]+right[3]+right[2]+right[3]+right[2]+right[4:] #expansion of right part 
            eOfRXorKey=int(eOfR,2)^int(uKey,2) #xor of key and expanded right part
            #convert xor into bit string
            while eOfRXorKey>0:
                binaryxor+=str(eOfRXorKey%2)
                eOfRXorKey=eOfRXorKey//2
            if len(binaryxor)<8:
                while len(binaryxor)<8:
                    binaryxor+='0'
            binaryxorFinal=binaryxor [reverse_slice]
            #print("The left part of the text is:"+left)
            #print("The key for the round is:"+uKey)
            #print("The right part of the text is:"+right)
            #print("The expanded right part is:"+eOfR)
            #print("The xor of key and expansion is :"+binaryxorFinal)
            nibbleL=binaryxorFinal[:4]
            nibbleR=binaryxorFinal[4:]
            #print("Input for S1 is :"+nibbleL)
            #print("Input for S2 is:"+nibbleR)
            #Computation of S box output
            S1Output=S1[nibbleL]
            S2Output=S2[nibbleR]
            SBoxOutput=S1Output+S2Output
            #print("Output for the S box is:"+SBoxOutput)
            #xor of left and output from s box
            rightNextRound=int(SBoxOutput,2)^int(left,2)
            #convert right next round into bit string
            while rightNextRound>0:
                binaryRight+=str(rightNextRound%2)
                rightNextRound=rightNextRound//2
            if len(binaryRight)<6:
                while len(binaryRight)<6:
                    binaryRight+='0'
            binaryRightFinal=binaryRight [reverse_slice]
            #print("ouptut of final xor of left and right:"+binaryRightFinal)
            #print("The right part of the next round is:"+binaryRightFinal)
            #print("The left part for the next round is:"+right)
            left=right
            right=binaryRightFinal
            binaryxor=''
            binaryRight=''
            round=round+1
        finalEncryptedString+=right+left
        print("The final output for round "+str(round)+" is:"+right+left)
        round=0
    print("The final encrypted string is:"+finalEncryptedString)
    return finalEncryptedString
