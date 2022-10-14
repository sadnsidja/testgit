foodlist = []
def showlist():
    print("---my Menu---")
    total = 0
    for i in range(len(foodlist)):
        print(foodlist[i][0],foodlist[i][1],"THB")
        total += foodlist[i][1]
    print("Total",total,'THB')
while True:
    menuName = input("MenuName>>>")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("MenuPrice>>>"))
        foodlist.append([menuName,menuPrice])
print(foodlist)
showlist()