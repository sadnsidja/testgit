userinput = int(input("number>>>"))

for x in range(userinput):
    print(" "*(userinput-x),"*"*(x+1)+"*"*x)