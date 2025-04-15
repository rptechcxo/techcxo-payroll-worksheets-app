import holidays
from datetime import date, datetime, timedelta
from openpyxl import Workbook


MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def worksheet_name(wb: Workbook, expected_sheet_name: str):
    sheet_name_list = [sheet.strip() for sheet in wb.sheetnames]
    for i in range(len(sheet_name_list)):
        if expected_sheet_name == sheet_name_list[i].strip():
            return sheet_name_list[i]

    return None


def find_cell(ws, target_value: str, regex: bool=False) -> tuple[int, int] | None:
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            if cell.value is None:
                continue
            elif target_value in cell.value:
                return (cell.row, cell.column)

    return None


def get_adjusted_tenth(date_str, country='US', state=None):
    """
    Given a date string, returns the adjusted 10th day of the following month,
    formatted as 'Mon 10th', where the suffix is adjusted properly and the
    month is abbreviated.

    The 10th is chosen from the next month of the given date. If the 10th falls
    on a weekend or a bank holiday (based on country and optional state),
    the function finds the closest previous weekday that is not a holiday.

    Parameters:
    - date_str (str): The input date in 'YYYY-MM-DD' format.
    - country (str): Country code for holidays (default 'US').
    - state (str or None): Optional state code (e.g., 'CA') for localized holidays.

    Returns:
    - str: Adjusted date formatted like 'Feb 10th'.
    """

    def day_suffix(day):
        if 11 <= day <= 13:
            return "th"
        return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

    # Convert input date
    base_date = datetime.strptime(date_str, "%Y-%m-%d")

    # Move to next month
    if base_date.month == 12:
        target_month = 1
        target_year = base_date.year + 1
    else:
        target_month = base_date.month + 1
        target_year = base_date.year

    # Holiday calendar
    holiday_calendar = holidays.country_holidays(country, years=target_year, subdiv=state)

    # Start at the 10th
    target_date = datetime(target_year, target_month, 10)

    # Adjust backwards for weekends or holidays
    while target_date.weekday() >= 5 or target_date in holiday_calendar:
        target_date -= timedelta(days=1)

    # Format output like "Feb 10th"
    suffix = day_suffix(target_date.day)
    formatted = target_date.strftime(f"%b {target_date.day}{suffix}")
    return formatted


def duplicate_worksheet(wb: Workbook, sheet_name: str, save_path: str):
    """
    Duplicates a worksheet in an Excel workbook.

    Args:
        wb (Workbook): The workbook object.
        sheet_name (str): The name of the sheet to duplicate.

    Returns:
        str: The name of the new duplicated sheet.
    """
    orig_ws = wb[wb.sheetnames[0]]
    ws = wb.copy_worksheet(orig_ws)
    ws.title = sheet_name
    s = find_cell(ws, "December")
    for row in ws.iter_rows(min_row=s[0]+1, max_row=s[0]+23, min_col=s[1], max_col=s[1]+12):
        for cell in row:
            cell.value = None
            cell.comment = None
            cell.number_format = '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'
    
    for row in ws.iter_rows(min_row=s[0]-1, max_row=s[0]-1, min_col=s[1], max_col=s[1]+12):
        for cell in row:
            cell.value = None

    wb.move_sheet(wb[sheet_name], offset=-len(wb.sheetnames)+1)
    wb.save(save_path)


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
