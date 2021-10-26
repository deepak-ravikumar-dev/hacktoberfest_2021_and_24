# Construct a DFA for the language of strings over {a,b} in the form a^n*b^n ,where n,m>=0
def q0(char):
    if(char=='a'):
        pos=1
    elif(char=='b'):
        pos=3
    else:
        pos=-1 #it is used to check any invalid symbol
    return pos

def q1(char):
    if(char=='a'):
        pos=1
    elif(char=='b'):
        pos=2
    else:
        pos=-1
    return pos

def q2(char):
    if(char=='a'):
        pos=3
    elif(char=='b'):
        pos=2
    else:
        pos=-1
    return pos

def q3(char):
    if(char=='a'):
        pos=3
    elif(char=='b'):
        pos=3
    else:
        pos=-1
    return pos

def checkValid(str):
    l=len(str)
    pos=0
    for i in range(l):
        if(pos==0):
            pos=q0(str[i])
        elif(pos==1):
            pos=q1(str[i])
        elif(pos==2):
            pos=q2(str[i])
        elif(pos==3):
            pos=q3(str[i])
        else:
            return 0
    if(pos==2):
        return 1
    else:
        return 0

print("Enter your string: ")
s=input()
if(checkValid(s)):
    print("Accepted")
else:
    print("Not Accepted")