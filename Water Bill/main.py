ccode = input("Enter customer's code: ").lower()
cbmeter = int(input("Enter the customer's beginning meter reading: "))
cemeter = int(input("The customer's ending meter reading: "))
gallons = 0
cost = 0
if (999999999 > cemeter > 0) or (999999999 > cbmeter > 0):
    if (ccode == 'r') or (ccode == 'c') or (ccode == 'i'):
        if (cemeter < cbmeter):
            gallons = ((1000000000 + cemeter) - cbmeter) * .1
        elif cemeter > cbmeter:
            gallons = (cemeter - cbmeter) * .1
        if (ccode == 'r'):
            cost = 5 + (gallons * 0.0005)
        elif (ccode == 'c'):
            if (gallons <= 4000000):
                cost = 1000
            elif (gallons > 4000000):
                cost = 1000 + ((gallons - 4000000) * 0.00025)
        elif (ccode == 'i'):
            if (gallons <= 4000000):
                cost = 1000
            elif (4000000 > gallons > 10000000):
                cost = 2000
            elif (gallons > 10000000):
                cost = 2000 + ((gallons - 10000000) * .00025)
    print("Customer code:", ccode)
    print("Beginning meter reading:", "{:0>9}".format(cbmeter))
    print("Ending meter reading:\t", "{:0>9}".format(cemeter))
    if (ccode != 'r') and (ccode != 'c') and (ccode != 'i'):
        print("Invalid Entry")
    print(F"Gallons of water used: {gallons:.2f}")
    print(f"Amount billed: ${cost:.2f}")
else:
    print("ERROR! Please enter a number from 0 - 999,999,999")




