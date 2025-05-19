# Payroll Worksheet App

Assumptions
1. The header for table always start on line 2
1. Column W is always the last column of the table


## Test Build

```bash
poetry install --with build
poetry run pyinstaller --onefile --name "payroll-worksheets" src/app/main.py --hidden-import=holidays.countries
```
