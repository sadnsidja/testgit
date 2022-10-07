def VatCalcylate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(VatCalcylate(int(input())))