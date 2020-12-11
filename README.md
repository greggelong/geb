# geb
A place to hold some code inspired by reading Gödel, Escher, Bach:  by Douglas Hofstadter.


## MU Puzzle

The MU puzzle is a formal system that Hofstadter has us play with to get familiar with formal systems. 

MU has an 3 characters 'M', 'U', 'I'

MU has as its axiom 'MI'

MU has four rules:
>RULE I: If you possess a string whose last letter is 1, you can add on a U at
the end

>RULE II: Suppose you have Mx. Then you may add Mxx to your collection.

>RULE III: If III occurs in one of the strings in your collection, you may
make a new string with U in place of III.

>RULE IV: If UU occurs inside one of your strings, you can drop it

rule one can be captured by:
```python
# rule 1
    if testString[-1] == "I":
        nextgen.append(("from rule 1",testString + "U"))

```
rule two: As M only ever appears at the start of a string it can be captured by:
```python

# rule 2
    if testString[0] == "M":
        nextgen.append(("from rule 2",testString+testString[1:]))

```
Rules 3 and 4 are a little different.

In order to code this formal stystem I am writing my own replacement algorithm for rule 3 and rule 4, 
as replace() or regex would only catch one instance (two if you, reverse it) (see previous code. mupuzzle1-6.py)

But we need to get every possible instance of 'III' or 'UU'

It really seems that built in replace() is more for natural languages in these languages you rarely need to pick every set of three out of four or more identical characters.

This actually highlights the character of formal languages and mechanical manipulation. So it's fitting that
I must use a lower level approach to capture this and get all possible instances.

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

H. repeatedly highlights the important differences between formal and ordinary language

>Such strings, producible by the rules, are
>called theorems. The term "theorem" has, of course, a common usage in
>mathematics which is quite different from this one. 
>It means some statement in ordinary language which has been proven to be true by a rigorous
>argument, such as Zeno's Theorem about the "unexistence" of motion, or
>Euclid's Theorem about the infinitude of primes. But in formal systems,
>theorems need not be thought of as statements-they are merely strings of
>symbols. And instead of being proven, theorems are merely produced, as ifby
>machine, according to certain typographical rules.
      
      
