# verify and ensure debit card number is 14
# year should be 2020 or greater than 2020 if below 2020 it is expired
# month should be in 1 to 12 if other numbers it is invalid
# cvv number should be length of 3 digits

debit_card = int(input("Enter debit card number: "))
debit_card_str = str(debit_card)
if len(debit_card_str) < 14 or len(debit_card_str) > 14:
    print("This card details are invalid: ", debit_card_str)
else:
    print("This card details are valid: ", debit_card_str)

year = int(input("Enter the year of debit card: "))

if year >= 2020:
    print("Your card year is valid:", year)
else:
    print("Your card year is expired:", year)

month = int(input("Enter the month range: "))
# month_str = str(month)
if month <= 1 or month >= 12:
    print("Month is invalid:", month)
else:
    print("Month is valid:", month)

cvv = int(input("Enter cvv number: "))
cvv_str = str(cvv)

if len(cvv_str) == 3:
    print("your cvv number is valid", cvv_str)
else:
    print("Your cvv number is invalid:", cvv_str)
