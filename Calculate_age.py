from dateutil.relativedelta import relativedelta
from datetime import datetime

# Ask for date of birth
year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

# Calculate age
dob = datetime(year, month, day)
age = relativedelta(datetime.now(), dob)

# Print age in years, months, and days
print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
