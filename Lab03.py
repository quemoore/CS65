# Quentin Moore
# CS 65 Section 1
# 9/11/2024

bill_year = float(input("Enter a year: "))
serial_number = int(input("Enter the serial number: "))

if bill_year < 2006 or bill_year >= 2025:
    print("COUNTERFEIT")
elif bill_year % 2 == 0 and serial_number % 3 == 0:
    print("LEGITIMATE")
elif bill_year % 2 != 0 and serial_number % 5 == 0:
    print("LEGITIMATE")
else:
    print("COUNTERFEIT")
