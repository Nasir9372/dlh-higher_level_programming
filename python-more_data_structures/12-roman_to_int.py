#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    if not isintance(roman_string, str) or if roman_string is None:
        return 0

    total = 0

    for i in range(len(roman_string)):
        c_v = roman[roman_string[i]]

        # check next value if it exists
        if i + 1 < len(roman_string):
            n_v = roman[roman_string[i + 1]]

            if c_v < n_v:
                total -= c_v
            else:
                total += c_v
        else:
            # last character always add
            total += c_v

    return total
