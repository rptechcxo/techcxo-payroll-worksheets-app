# Requirements

Input: requirements-docs/<YYYY-MM-DD> Payroll (Monthly).xlsx

Ouput: [for <Partner Last Name> in requirements-docs/<Partner Last Name> Pay Worksheet.xlsx]

Manipulations: 
- Transpose the row associated with the Partner into a new column in the Partner Pay Worksheet.
The mapping is one to one except:
- Bonus Revenue + Bonus Equity = Bonus
- Short Term Disability -> Child Voluntary is from the "Deduction Report" tabl
- match on cdeductdecs and copy namount
- Copy comments on Partner Receiveable, A/R both, Other Adjustment

Resources will be
- Windows VM for dev
- Same packaging as last time

Issues:
- Date in row 5 is 10th or day prior or after, cant be weekend, or Bank Holidays
- 