from pandera import DataFrameSchema, Column, Index
from pandera.dtypes import Float, String


_details_schema = {
    ("Guaranteed Payments", "Internal Time"): Column(Float, nullable=True, coerce=True),
    ("", "Earnings"): Column(Float, nullable=True, coerce=True),
    ("Bonus", "Revenue"): Column(Float, nullable=True, coerce=True),
    ("Bonus", "Equity"): Column(Float, nullable=True, coerce=True),
    ("1099 Compensation", "15th"): Column(Float, nullable=True, coerce=True),
    ("", "31st"): Column(Float, nullable=True, coerce=True),
    ("Expense", "Reimburse"): Column(Float, nullable=True, coerce=True),
    ("Safe Harbor", "Withheld"): Column(Float, nullable=True, coerce=True),
    ("Profit Sharing", "Withheld"): Column(Float, nullable=True, coerce=True),
    ("Partner", "Receivable"): Column(Float, nullable=True, coerce=True),
    ("401(k) loan", "repayment"): Column(Float, nullable=True, coerce=True),
    ("Roth 401(k)", "Deduction"): Column(Float, nullable=True, coerce=True),
    ("Pre-tax 401(k)", "Deduction"): Column(Float, nullable=True, coerce=True),
    ("Group", "Health"): Column(Float, nullable=True, coerce=True),
    ("", "Dental"): Column(Float, nullable=True, coerce=True),
    ("", "Vision"): Column(Float, nullable=True, coerce=True),
    ("", "LTD"): Column(Float, nullable=True, coerce=True),
    ("Admin", "Fee"): Column(Float, nullable=True, coerce=True),
    ("A/R", "Backouts"): Column(Float, nullable=True, coerce=True),
    ("A/R", "Addbacks"): Column(Float, nullable=True, coerce=True),
    ("Other", "Adjustments"): Column(Float, nullable=True, coerce=True),
    ("", "Total Pay"): Column(Float, nullable=True, coerce=True),
}


DetailsSchema = DataFrameSchema(
    columns=_details_schema,
)

_deduction_report_schema = {
    "namount": Column(Float, nullable=True, coerce=False),
    "cdeductcode": Column(String, nullable=False),
}

DeductionReportSchema = DataFrameSchema(
    columns=_deduction_report_schema,
    index=Index(String, name="ceecode")
)
