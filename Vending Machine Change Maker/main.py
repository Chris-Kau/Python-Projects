import math
changeCounter = [0,0,0,0,0]
def checkChange(x, y):
    if x > 0:
        return (f"{x} {y}\n   ")
    else:
        return ''
def menu():
    print(f"Stock contains:\n   {coinStock[4]} nickels\n   {coinStock[3]} dimes\n   {coinStock[2]} quarters\n   {coinStock[1]} ones\n   {coinStock[0]} fives")

def formattedPaymentDue(x, y, z):
    if z == 1:
        if x <= 0:
            print(f"Payment due: {y} cents")
        else:
            print(f"Payment due: {x} dollar(s) and {y} cents")
    elif z == 2:
        if x <= 0:
            print(f"Amount due is: {y} cents\n")
        else:
            print(f"Amount due is: {x} dollar(s) and {y} cents\n")
def change(x):
    # order goes fives, ones, quarters, dimes, nickels
    changeCounter = [0, 0, 0, 0, 0]
    rDollarCents = int(round(x, 0))
    absDollarCents = int(math.fabs(rDollarCents))
    initialAbsDollarCents = absDollarCents
    while absDollarCents != 0:
        if absDollarCents >= 25 and coinStock[2] > 0:
            absDollarCents -= 25
            changeCounter[2] += 1
            coinStock[2] -= 1
            continue
        elif absDollarCents >= 10 and coinStock[3] > 0:
            absDollarCents -= 10
            changeCounter[3] += 1
            coinStock[3] -= 1
            continue
        elif absDollarCents >= 5 and coinStock[4] > 0:
            absDollarCents -= 5
            changeCounter[4] += 1
            coinStock[4] -= 1
            continue
        break
    if (changeCounter[2] > 0 and coinStock[2] < 0) or (changeCounter[3] > 0 and coinStock[3] <= 0) or (changeCounter[4] > 0 and coinStock[4] <= 0):
        print(f"\nPlease take the change below.\n   {checkChange(int(changeCounter[2]), 'quarters')}{checkChange(int(changeCounter[3]), 'dimes')}{checkChange(int(changeCounter[4]), 'nickels')}",end='\n')
        amountDue = float((refundChange[0] * 5) + (refundChange[1]) + (refundChange[2] * 0.25) + (refundChange[3] * .1) + (refundChange[4] * 0.05)) - ((changeCounter[4] * 0.05) + (changeCounter[3] * .10) + (changeCounter[2] * .25) + centsOwe/100)
        print(f"Machine is out of change.\nSee store manager for remaining refund.")
        formattedPaymentDue(int(amountDue//1),int((amountDue%1) * 100), 2)
        menu()
        print()
    else:
        if initialAbsDollarCents > 0:
            print(f"\nPlease take the change below.\n   {checkChange(int(changeCounter[2]), 'quarters')}{checkChange(int(changeCounter[3]), 'dimes')}{checkChange(int(changeCounter[4]), 'nickels')}")
            menu()
        else:
            print("\nPlease take the change below.\n   No change due.\n")
            menu()
        print()
#order goes fives, ones, quarters, dimes, nickels
coinStock = [0,0,25,25,25]
print(f"Welcome to the vending machine change maker program\nChange maker initialized.\nStock contains:\n   {coinStock[4]} nickles\n   {coinStock[3]} dimes \n   {coinStock[2]} quarters\n   {coinStock[1]} ones\n   {coinStock[0]} fives\n")
while True:
    purchprice = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    totalVal = purchprice
    if purchprice == "q":
        totalCents = (coinStock[2] * 25) + (coinStock[3] * 10) + (coinStock[4] * 5)
        totalCentsToDollars = int(totalCents // 100)
        totalLeftOverCents = totalCents - (totalCentsToDollars * 100)
        print(f"Total: {(coinStock[0] * 5) + coinStock[1] + totalCentsToDollars} dollar(s) and {totalLeftOverCents} cents")
        break
    elif (float(purchprice) * 100 % 5 != 0) or (float(purchprice) < 0):
        print("Illegal Price: Must be a non-negative multiple of 5 cents.")
        continue
    else:
        refundChange = [0, 0, 0, 0, 0]
        fpurchprice = float(purchprice)
        print("\nMenu for deposits:\n    'n' - deposit a nickel\n    'd' - deposit a dime\n    'q' - deposit a quarter\n    'o' - deposit a one dollar bill\n    'f' - deposit a five dollar bill\n    'c' - cancel the purchase\n")
        onesOwe = int(fpurchprice // 1)
        centsOwe = int(round(((fpurchprice % 1) * 100),2))
        formattedPaymentDue(onesOwe, centsOwe, 1)
        while fpurchprice > 0:
            deposit = input("Indicate your deposit: ").lower()
            if(deposit == "n"):
                fpurchprice -= 0.05
                coinStock[4] += 1
                refundChange[4] += 1
            elif(deposit == "d"):
                fpurchprice -= 0.1
                coinStock[3] += 1
                refundChange[3] += 1
            elif (deposit == "q"):
                fpurchprice -= 0.25
                coinStock[2] += 1
                refundChange[2] += 1
            elif (deposit == "o"):
                fpurchprice -= 1
                coinStock[1] += 1
                refundChange[1] += 1
            elif (deposit == "f"):
                fpurchprice -= 5
                coinStock[0] += 1
                refundChange[0] += 1
            elif (deposit == "c"):
                #The reassigning of fpurchprice and dollarCents is just to get the updated value
                dollarCents = float(fpurchprice) * 100
                change(round(float(purchprice) - fpurchprice,2) * 100)
                break
            else:
                print(f"Illegal selection: {deposit}")
                continue
            onesOwe = int(fpurchprice // 1)
            centsOweUpdated = int(round(((fpurchprice % 1) * 100), 2))
            dollarCents = fpurchprice * 100
            if(fpurchprice > 0):
                formattedPaymentDue(onesOwe, centsOweUpdated, 1)
                continue
            else:
                change(dollarCents)
            continue