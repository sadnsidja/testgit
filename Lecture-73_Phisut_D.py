foodlist = []
menu = {"ข้าวมันไก่":40,"ข้าวไก่ทอด":45,'ข้าวหน้าเนื้อ':50,'ปลาทอด':100}
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
        foodlist.append([menuName,menu[menuName]])
print(foodlist)
showlist()