

genList = [["MI"]]


generation = 0



for i in range(5):
    print(i,genList)
    nextgen = []
    testList = genList[generation] # get the list of this generation
    generation +=1  # next generation
    nextgen= []
    genList.append(nextgen)
    
    for string in testList:
        testString = string
        
        # rule 2 can always be applied
        
        # rule 1
        if testString[-1] == "I":
            nextgen.append(testString + "U")
            
        # rule 2
        if testString[0] == "M":
            nextgen.append(testString+testString[1:])
            
        # rule 3
        if "III" in testString:
            # test maybe use a strg replace function or regex regular expressions
            #newStrg = strg.replace("III","U",1) # replaces just the first occurance, not great
            nextgen.append(testString.replace("III","U")) # replaces all still not very good
        
        #rule 4
            
        if "UU" in testString:
            # test maybe use a strg replace function or regex regular expressions
            #newStrg = strg.replace("UU","",1) # replaces just the first occurance, not great
            nextgen.append(testString.replace("UU","")) #
            
        
        
        
        
        