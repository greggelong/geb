# trying to get a better result using regex

import re 


def muRules(testString,nextgen):
    # rule 2 can always be applied
        
    # rule 1
    if testString[-1] == "I":
        nextgen.append(("from rule 1",testString + "U"))
        
    # rule 2
    if testString[0] == "M":
        nextgen.append(("from rule 2",testString+testString[1:]))
        
    # rule 3
    if "III" in testString:
        # test maybe use a strg replace function or regex regular expressions
        #newStrg = strg.replace("III","U",1) # replaces just the first occurance, not great
        nextgen.append(("from rule 3",re.sub(r"III",r"U",testString))) # replaces all still not very good
        
       # re.sub(r"(house|the house)", r"**\1**", mystring)
    
    #rule 4
        
    if "UU" in testString:
        # test maybe use a strg replace function or regex regular expressions
        #newStrg = strg.replace("UU","",1) # replaces just the first occurance, not great
        nextgen.append(("from rule 4",testString.replace("UU",""))) #
    

def transform(genList,gens):
    # keep track of generations 
    generation = 0
    for i in range(gens):
        #print(i,genList)
        nextgen = []
        testList = genList[generation] # get the list of this generation
        generation +=1  # next generation
        nextgen= []
        genList.append(nextgen)
        # check each string in current generation
        for string in testList:
            testString = string[1]
            muRules(testString,nextgen)
            
    


def printList():
    for i,g in enumerate(genList):
        print(i,g, len(g))
    



# axiom in tuple in a  2 dimenional list
genList = [[("axiom","MI")]]

transform(genList,5)
printList()






        
        
            
        
        

        
        