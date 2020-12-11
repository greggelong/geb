# geb
A place to hold some code inspired by reading Gödel, Escher, Bach:  by Douglas Hofstadter.


## MU Puzzle

In order to code this formal stystem I am writing my own replacement algorithm for rule 3 and rule 4, 
as replace() or regex would only catch one see previous code.

It really seems that built in replace() is more for natural languages in these languages you rarely need to pick every set of three out of four or more identical characters.

This actually highlights the character of formal languages and mechanical manipulation. So it's fitting that
I must use a lower level approach to capture that character and get all the groups.

Here is some example code. Of this approach for rule  3: replace any 'III' with 'U'

```python
strlst=[]

s='MIIIIIIII'
count=0

for i in range(len(s)-2):
    
    if s[i]=='I' and s[i+1] == 'I' and s[i+2]=='I':
        count+=1
        l = list(s)
        l[i] = "U"
        l[i+1] = ""
        l[i+2] =""
        strlst.append("".join(l))
        
        
        
print(count,strlst,len(strlst))

# >> 6 ['MUIIIII', 'MIUIIII', 'MIIUIII', 'MIIIUII', 'MIIIIUI', 'MIIIIIU'] 6
````

      
      
