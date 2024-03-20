import numpy
import pickle

def exchanger():
    file_path = "round.pkl"
    with open(file_path,"rb")as f:
            a = pickle.load(f)
    currencies = {
        "SGD": (1.0,1.0), #index 0 is x to sgd and 1 is sgd to x
        "USD" : (1.34,0.74),
        "GBP" : (1.70,0.59),
        "EUR" : (1.46,0.69),
        "JPY" : (0.0089,112.05),
        "CAD" : (0.99,1.01),
        "AUD" : (0.87,1.14),
        "CNY" : (0.19,5.36),
        "CHF" : (1.51,0.66),
        "HKD" : (0.17,5.83),
        "TRY" : (0.042,24.09),
        "ZWD" : (0.0036,269.53)
    }
    currencies
    print("Hello, welcome to the currency exchange")
    print("")
    print("what currency are you currently using")
    print("""
    SGD - Singapore Dollar
    USD - US Dollar    
    GBP - Brittish Pound
    EUR - Euro
    JPY - Japanese Yen
    CAD - Canadian Dollar
    AUD - Australian Dollar
    CNY - China Yuan
    CHF - Swiss Franc
    HKD - Hong Kong Dollar
    TRY - Turkish Lira
    ZWD - Zimbabwe Dollar
        """)
    print("Begin:")
    print("")
    begin = input("input *a* to begin or round to toggle rounding")
    if begin == 'round':
        roundask = input("you are about to toggle rounding feature, confirm? y/n")
        if roundask == 'y':
            if a == True:
                print("")
                print("rounding successfully deactivated")
                print("")
                file_path = "round.pkl"
                new_value = False
                with open(file_path, "wb") as f:
                    pickle.dump(new_value, f)
            if a == False:
                print("")
                print("rounding successfully activated")
                print("")
                file_path = "round.pkl"
                new_value = True
                with open(file_path, "wb") as f:
                    pickle.dump(new_value, f)
        if roundask == 'n':
            print("round toggle successfully cancelled")
    if begin == 'a':
        print("insert first currency")
    currency1 = input("insert currency")
    for currency,ratio in currencies.items():
        if currency1 == f'{currency}':
            print(f"{currency}")
            break
    print("insert value of first currency")
    currency1v = float(input("insert value of first currency"))
    print(f"{currency1v} {currency1} =>")
    print("insert desired currency")
    currency2 = input("insert desired currency")
    for currency,ratio in currencies.items():
        if currency1 == f'{currency}':
            print(f"{currency1v} {currency1} => {currency2}")
            break
    result1 = currencies[currency1][0] * currency1v
    result2 = result1 * currencies[currency2][1]
    if a == True:
        result2 = numpy.round(result2, decimals=2)
    print("")
    print(f"{currency1v} {currency1} is equal to {result2} {currency2}")