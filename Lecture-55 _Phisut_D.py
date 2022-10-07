def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    return int(input(">>"))

def vatCalculator(total):
    return total + (total * 7 / 100)

def priceCalculator():
    return int(input("First Product Price : "))+int(input("Second Product Price : "))

if login() == True:
    choose = showMenu()
    if choose == 1:
        print(vatCalculator(priceCalculator()))
    elif choose == 2:
        print(priceCalculator())
    else:
        print("ERROR")

else:
    print("ERROR")