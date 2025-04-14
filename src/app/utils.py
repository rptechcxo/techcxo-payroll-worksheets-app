import holidays
from datetime import date

def is_business_day(date_to_check: date, country_code:str = 'US'):
    """
    Checks if a given date is a business day, excluding weekends and bank holidays.

    Args:
        date_to_check (date): The date to check.
        country_code (str, optional): The ISO 3166-1 alpha-2 country code. Defaults to 'US'.

    Returns:
        bool: True if the date is a business day, False otherwise.
    """

    if date_to_check.weekday() >= 5:  # Saturday or Sunday
        return False

    country_holidays = holidays.country_holidays(country_code, years=date_to_check.year)
    if date_to_check in country_holidays:
        return False

    return True


# Example Usage:
"""
date_to_check = date(2025, 5, 26)  # Memorial Day 2025

if is_business_day(date_to_check, country_code='US'):
    print(f"{date_to_check} is a business day.")
else:
    print(f"{date_to_check} is not a business day.")

# Find the next business day
current_date = date(2025, 5, 26)
while not is_business_day(current_date):
    current_date += timedelta(days=1)

print(f"The next business day is: {current_date}")
"""