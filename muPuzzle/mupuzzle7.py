# trying to get a better result using regex
# added a second rule for 3 3a to get it reversed

import re 


def muRules(testString,nextgen):
    #takes string and the next gen list from transform function
    
    # rule 2 can always be applied
        
    # rule 1
    if testString[-1] == "I":
        nextgen.append(("from rule 1",testString + "U"))
        
    # rule 2
    if testString[0] == "M":
        nextgen.append(("from rule 2",testString+testString[1:]))
        
    ''' rule 3
      here I am writing my own replacement algorithm for rule 3 and rule 4, as replace() or regex would only catch one see previous code
      seems that built in replace() is more for natural languages that rarely need to pick every set of three out of four or more identical characters.
      This actually highlights the character of formal languages and mechanical manipulation. so it's fitting that
      i must use a lower level approach to capture that character and get all the groups
    '''
    for i in range(len(testString)-2):  #for each character in string less the length i am looking
    
        if testString[i]=='I' and testString[i+1] == 'I' and testString[i+2]=='I':   #test 3 characters at a time
             
            l = list(testString)  # convert to a mutable list
            l[i] = "U"            #make changes
            l[i+1] = ""
            l[i+2] =""
            nextgen.append(("from rule 3","".join(l)))  #convert back to a string and append as a tuple with explantion 
     
    
    #rule 4
        
    for i in range(len(testString)-1):  # 
    
        if testString[i]=='U' and testString[i+1] == 'U':
             
            l = list(testString)    # convert to a list 
            l[i] = ""
            l[i+1] = ""
             
            nextgen.append(("from rule 4","".join(l)))
    

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

transform(genList,4)
printList()






        
        
            
        
        

        
        