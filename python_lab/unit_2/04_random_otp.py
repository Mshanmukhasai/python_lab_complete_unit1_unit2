# Generate a random OTP
# User chooses 4 or 6 digits

import random

digits = int(input("Enter the number of OTP digits (4 or 6): "))

if digits == 4 or digits == 6:
    otp = random.randint(10 ** (digits - 1), 10 ** digits - 1)
    print("Generated OTP:", otp)
else:
    print("Please enter only 4 or 6.")
