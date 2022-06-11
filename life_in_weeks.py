age = input("What is your current age?\n")

age_as_int = int (age)

days_remaining = age_as_int * 365
weeks_remaining = age_as_int * 52
months_remaining = age_as_int * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left!"

print(message)