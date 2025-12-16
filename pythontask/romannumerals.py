def transform(j):
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    result = []
    for value, numeral in roman_numerals:
        while j >= value:
            result.append(numeral)
            j -= value
    return ''.join(result)
# Example usage:
number = int(input("Enter an integer to convert to Roman numeral: "))
roman_numeral = transform(number)
print(f"The Roman numeral for {number} is: {roman_numeral}")