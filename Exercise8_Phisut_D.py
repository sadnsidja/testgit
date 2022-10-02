UserName = input("UserName>>>")
PassWord = int(input("PassWord>>>"))
if UserName == "TheOne" and PassWord == 1234:
    print("Welcome to shop",UserName)
    print("______SHOP______")
    print("1.apple  20 THB")
    print("2.orange 30 THB")
    ChooseFruit = int(input("ChooseFruit>>>"))
    if ChooseFruit == 1:
        print(UserName,"buy a apple")
    else:
        print(UserName,"buy a orange")