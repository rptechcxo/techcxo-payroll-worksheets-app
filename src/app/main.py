from logging import basicConfig, getLogger, INFO
from app.extraction import import_tables
from glob import glob
from os import path
from openpyxl import load_workbook


logger = getLogger(__name__)
basicConfig(
    level=INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


def main():
    inputs = {
        "data_path": "requirement-docs/2025-01-31 Payroll (Monthly).xlsx",
        "partner_worksheet_folder": "worksheets",
        "year_month": "2025-02-10",
    }
    details, deductions = import_tables(inputs["data_path"])

    partner_list = glob(path.join(
        inputs["partner_worksheet_folder"],
        "*.xlsx"
    ))
    for partner in partner_list:
        worksheet = load_workbook(partner)


if __name__ == "__main__":
    main()
