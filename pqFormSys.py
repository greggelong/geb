x= ""
y= ""
z=""

for i in range(5):
    x = x + "-"
    y = ""
    for j in range(5):
        y = y + '-'
        
        z= "-" * (len(x)+len(y))
        print("Meaning ",len(x), "+",len(y),"=", len(z))
        print(x+"p"+y+"q"+z)    
