def calculateCompoundInterest():
    
# This first 3 lines are provided for you
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))

    a = round((client_one_principal*((1 + (client_one_rate/100))**client_one_time)),2)
    ci = round(a - client_one_principal,1)
    print("Compound Interest: " + str(ci))
    print("---")

    client_two_principal = float(input("Principle (amount): "))
    client_two_time =      float(input("Time:               "))
    client_two_rate =      float(input("Rate:               "))

    a = round((client_two_principal*((1 + (client_two_rate/100))**client_two_time)),2)
    ci = round(a - client_two_principal,2)
    print("Compound Interest: " + str(ci))
    print("---")

    client_three_principal = float(input("Principle (amount): "))
    client_three_time =      float(input("Time:               "))
    client_three_rate =      float(input("Rate:               "))

    a = round((client_three_principal*((1 + (client_three_rate/100))**client_three_time)),2)
    ci = round(a - client_three_principal,1)
    print("Compound Interest: " + str(ci))
# end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
