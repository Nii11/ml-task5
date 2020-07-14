# %%
import re

# %%
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""   
    for ele in s:  
        str1 += ele   
    return str1  

# %%
file=input("log file location")
dfile=open('datafile.csv', "a+")
dfile.write(ip,date,error)
dfile.close()
# %%
f=open(file, "r")

# %%
for l in f:
    if l.rstrip():
        ip=listToString(re.findall(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', l))
        date=listToString(re.findall(r'\d{1,2}\/[A-Z][a-z]{1,2}\/\d{1,4}\:\d{1,2}\:\d{1,2}\:\d{1,2}\s\+\d{1,4}|\[\d{1,2}\/[A-Z][a-z]{1,2}\/\d{1,4}\:\d{1,2}\:\d{1,2}\:\d{1,2}\s\-\d{1,4}',l))
        error=listToString(re.findall(r'\s\d{1,3}\s',l))
        en=ip+","+date+","+error
        dfile=open('datafile.csv', "a+")
        dfile.write(en+ "\n")
        dfile.close()
        l=+1
        

# %%

