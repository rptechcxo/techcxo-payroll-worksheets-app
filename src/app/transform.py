from typing import List
from pandas import DataFrame


_output_map = {
    "Internal Time": [("Guaranteed Payments", "Internal Time")],
    "Earnings": [("", "Earnings")],
    "Bonus": [("Bonus", "Revenue"), ("Bonus", "Equity")],
    "Expense Reimbursement": [("Expense", "Reimburse")],
    "401(k) deferral: Pre-tax": [("Pre-tax 401(k)", "Deduction")],
    "401(k) deferral: Roth": [("Roth 401(k)", "Deduction")],
    "401(k) Profit Sharing": [("Profit Sharing", "Withheld")],
    "401(k) Safe Harbor": [("Safe Harbor", "Withheld")],
    "401(k) Loan Repayment": [("401(k) loan", "repayment")],
    "Health insurance": [("Group", "Health")],
    "Dental insurance": [("", "Dental")],
    "Vision insurance": [("", "Vision")],
    "LTD insurance": [("", "LTD")],
    "Short Term Disability Ins.": ["ST2"],
    "HSA Deduction": ["KHA"],
    "Employee Voluntary Life Ins.": ["EVL"],
    "Spouse Voluntary Life Ins.": ["SVL"],
    "Child Voluntary Life Ins.": ["CVL"],
    "Partner Receivable": [("Partner", "Receivable")],
    "A/R Backouts": [("A/R", "Backouts")],
    "A/R Addbacks": [("A/R", "Addbacks")],
    "Admin Fee": [("Admin", "Fee")],
    "Other Adjustments": [("Other", "Adjustments")]
}


def data_to_worksheet(detail_data: DataFrame, deduction_data: DataFrame) -> List:
    output = []
    for key in _output_map:
        temp = 0.0
        # print(f"{_output_map[key][0] = }")
        if isinstance(_output_map[key][0], tuple):
            for indices in _output_map[key]:
                temp = temp + detail_data.loc[indices].item()
        elif isinstance(_output_map[key][0], str):
            for index in _output_map[key]:
                if index in deduction_data.index:
                    temp = temp - deduction_data.loc[index]["namount"]
        else:
            raise ValueError(f"Key {key} not found in either detail_data or deduction_data")
        output.append(temp)

    return output
