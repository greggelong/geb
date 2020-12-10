import random

def rule1(strg):
    ''' adds U to the end if strg ends in I'''
    print("chose 1")
    if strg[-1] == "I":
        newStrg = strg + "U"
        return(newStrg)
    else:
        print("can not apply rule 1")
        return(strg)

def rule2(strg):
    '''double after M M will seems
        only be at the start
        so i dont need to check for anything just double from index
        one
        "hello"+"hello"[1:]
        "helloello"'''
    print("chose 2")
    return strg+strg[1:]


def rule3(strg):
    ''' replaces III with U'''
    print("chose 3")
    if "III" in strg:
        # test maybe use a strg replace function or regex regular expressions
        #newStrg = strg.replace("III","U",1) # replaces just the first occurance, not great
        newStrg = strg.replace("III","U") # replaces all still not very good
        return(newStrg)
    else:
        print("cant apply 3")
        return(strg)

def rule4(strg):
    ''' replaces UU with "" '''
    print("chose 4")
    if "UU" in strg:
        # test maybe use a strg replace function or regex regular expressions
        #newStrg = strg.replace("UU","",1) # replaces just the first occurance, not great
        newStrg = strg.replace("UU","") # replaces all
        return(newStrg)
    else:
        print("cant apply rule 4")
        return(strg)




def randrule(strng):
    choice = random.randint(0,3)
    
    if choice == 0:
        return rule1(strng)
    elif choice ==1:
        return rule2(strng)
    elif choice == 2:
        return rule3(strng)
    elif choice ==3:
        return rule4(strng)
    return strng 
        
        
    
    


axiom = "MI"

gen = axiom
print(0, gen)
for i in range(1,20):
    gen = randrule(gen)
    print(i,gen)
print(randrule(gen))

