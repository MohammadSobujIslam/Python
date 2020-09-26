import re
txt="The /*rain in Spains"
#x=re.search("^The.*Spain$",txt)
x=re.search("^The",txt)
if x:
    print("YES! We have match!")
else:
    print("No match!")    
#print(x)
#y=re.findall("ai",txt)
#print(y)
#z=re.split("\s",txt)
#z3=re.split("\s",txt,2)
#print(z,z3)
'''
n=re.sub("/*",'',txt)

if n:
    print("YES! i have multiline comments")
else:
    print("No comments!")  
print(n)
'''
m=re.findall("/* | */",txt)
if m:
    print("YES! i have multiline comments")
else:
    print("No comments!")  
