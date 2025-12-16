def validate_card_number(card_no):
    return len(card_no) == 14 and card_no.isdigit()

def validate_expiry_year(year):
    return len(year) == 4 and year.isdigit() and 2020 <= int(year) <= 2030

def validate_expiry_month(month):
    return len(month) == 2 and month.isdigit() and 1 <= int(month) <= 12

def validate_cvv(cvv):
    return len(cvv) == 3 and cvv.isdigit()

def validate_name(name):
    return len(name) > 0 and all(x.isalpha() or x.isspace() for x in name)


# ---- Main Program ----
card_no = input("Enter your debit card number: ")
year = input("Enter the expiry year (YYYY): ")
month = input("Enter the expiry month (MM): ")
cvv = input("Enter the CVV: ")
name = input("Enter the name on the card: ")

if (
    validate_card_number(card_no)
    and validate_expiry_year(year)
    and validate_expiry_month(month)
    and validate_cvv(cvv)
    and validate_name(name)
):
    print("\nDebit Card Details are VALID ")
else:
    print("\nDebit Card Details are INVALID ")
