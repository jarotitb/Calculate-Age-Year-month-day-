Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from dateutil.relativedelta import relativedelta
... from datetime import datetime
... 
... # Ask for date of birth
... year = int(input("Enter year of birth: "))
... month = int(input("Enter month of birth: "))
... day = int(input("Enter day of birth: "))
... 
... # Calculate age
... dob = datetime(year, month, day)
... age = relativedelta(datetime.now(), dob)
... 
... # Print age in years, months, and days
... print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
