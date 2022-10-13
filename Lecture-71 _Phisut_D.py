listname = []
listprice = []
def showlist():
    for i in range(len(listname)):
        print(listname[i],listprice[i])
def totalprice():
    total = 0
    for x in range(len(listprice)):
        total += listprice[x]
    print("total",total)
while True:
    menuName = input("Name>>>")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price>>>"))
        listname.append(menuName)
        listprice.append(menuPrice)
print("---my foods---")
showlist()
totalprice()