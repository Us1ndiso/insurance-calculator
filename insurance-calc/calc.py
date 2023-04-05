oop = int(input("oop "))
deductable = int(input("deductable "))
coinsurance = float(input("coinsurance "))
surgery_price = int(input("surgery price "))

afterdeductable = surgery_price - deductable
surgery_priceforpatient = afterdeductable * coinsurance + deductable
companypays = surgery_price - surgery_priceforpatient
print(surgery_priceforpatient)
print(companypays)