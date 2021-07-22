income = int(input())

if 0 <= income <= 15527:
    percent = 0
    calculated_tax = round(income * percent)
    print(f"The tax for {income} is 0%. That is {calculated_tax} dollars!")
elif 15528 <= income <= 42707:
    percent = 0.15
    calculated_tax = round(income * percent)
    print(f"The tax for {income} is 15%. That is {calculated_tax} dollars!")
elif 42708 <= income <= 132406:
    percent = 0.25
    calculated_tax = round(income * percent)
    print(f"The tax for {income} is 25%. That is {calculated_tax} dollars!")
elif 42708 <= income <= 132406:
    percent = 0.25
    calculated_tax = round(income * percent)
    print(f"The tax for {income} is 25%. That is {calculated_tax} dollars!")
elif income >= 132407:
    percent = 0.28
    calculated_tax = round(income * percent)
    print(f"The tax for {income} is 28%. That is {calculated_tax} dollars!")
