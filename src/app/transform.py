df_to_output_map = {
    ('Guaranteed Payments', 'Internal Time') : "Internal Time",
    (                   '',      'Earnings') : "Earnings",
    (              'Bonus',       'Revenue') : "Bonus",
    (              'Bonus',        'Equity') : "Bonus",
    (            'Expense',     'Reimburse') : "Expense Reimbursement",
    (     'Pre-tax 401(k)',     'Deduction') : "401(k) deferral:  Pre-tax",
    (        'Roth 401(k)',     'Deduction') : "401(k) deferral:  Roth",
    (     'Profit Sharing',      'Withheld') : "401(k) Profit Sharing",
    (        'Safe Harbor',      'Withheld') : "401(k) Safe Harbor",
    (        '401(k) loan',     'repayment') : "401(k) Loan Repayment",
    (              'Group',        'Health') : "Health insurance",
    (                   '',        'Dental') : "Dental insurance",
    (                   '',        'Vision') : "Vision insurance",
    (                   '',           'LTD') : "LTD insurance",
    (            'Partner',    'Receivable') : "Partner Receivable",
    (                'A/R',      'Backouts') : "A/R Backouts",
    (                'A/R',      'Addbacks') : "A/R Addbacks",
    (              'Admin',           'Fee') : "Admin Fee",
    (              'Other',   'Adjustments') : "Other Adjustments",
}


ceecode_to_output_map = {
    "ST2" : "Short Term Disability Ins. ",
    "KHA" : "HSA Deduction",
    "EVL" : "Employee Voluntary Life Ins.",
    "SVL" : "Spouse Voluntary Life Ins.",
    "CVL" : "Child Voluntary Life Ins.",
}


pay_worksheet_desc = [
    "Internal Time",
    "Earnings",
    "Bonus",
    "Expense Reimbursement",
    "401(k) deferral:  Pre-tax",
    "401(k) deferral:  Roth",
    "401(k) Profit Sharing",
    "401(k) Safe Harbor",
    "401(k) Loan Repayment",
    "Health insurance",
    "Dental insurance",
    "Vision insurance",
    "LTD insurance",
    "Short Term Disability Ins. ",
    "HSA Deduction",
    "Employee Voluntary Life Ins.",
    "Spouse Voluntary Life Ins.",
    "Child Voluntary Life Ins.",
    "Partner Receivable",
    "A/R Backouts",
    "A/R Addbacks",
    "Admin Fee",
    "Other Adjustments"
]

