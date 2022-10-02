UserName = input("UserName>>>")
PassWord = int(input("PassWord>>>"))
total = 0
if UserName == "TheOne" and PassWord == 1234:
    print("Welcome to shop",UserName)#shop
    print("______SHOP______")
    print("1.apple  20 THB")
    print("2.orange 30 THB")
    ChooseFruit = int(input("1-2>>>"))#input 1
    if ChooseFruit == 1:
        total += 20
        print(UserName, "buy a apple 20 THB","total",total,"THB")
        ChooseFruit2 = int(input("1-2>>>"))#input 1.1
        if ChooseFruit2 == 1:
            total += 20
            print(UserName, "buy a apple 20 THB", "total", total,"THB")
        elif ChooseFruit2 == 2:
            total += 30
            print(UserName,"buy a orange 30 THB","total",total,"THB")
    elif ChooseFruit == 2:
        total += 30
        print(UserName,"buy a orange","total",total,"THB")
        ChooseFruit2 = int(input("1-2>>>"))#input 2
        if ChooseFruit2 == 1:
            total += 20
            print(UserName, "buy a apple 20 THB","total",total,"THB")
        elif ChooseFruit2 == 2:
            total += 30
            print(UserName,"buy a orange 30 THB","total",total,"THB")

