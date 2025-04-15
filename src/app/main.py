from logging import basicConfig, getLogger, INFO
from app.utils import worksheet_name, find_cell, MONTH, get_adjusted_tenth, duplicate_worksheet
from app.extraction import import_tables
from app.transform import data_to_worksheet
from glob import glob
from os import path
from openpyxl import load_workbook
from pandas import Series
from datetime import datetime, timedelta

logger = getLogger(__name__)
basicConfig(
    level=INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


def main():
    inputs = {
        "data_path": "requirement-docs/2025-01-31 Payroll (Monthly).xlsx",
        "partner_worksheet_folder": "requirement-docs/worksheets",
        "year_month": "2025-12-31",
    }
    year_month = datetime.strptime(inputs["year_month"], "%Y-%m-%d") + timedelta(days=28)

    partner_list = glob(path.join(
        inputs["partner_worksheet_folder"],
        "*.xlsx"
    ))
    
    for partner in partner_list:
        wb = load_workbook(partner)
        year = year_month.strftime("%Y")
        
        sheet_name = worksheet_name(wb, year)
        if sheet_name is None:
            logger.warning(f"Sheet {year} not found in <{path.basename(partner)}>")
            logger.info(f"Creating new Sheet {year} in <{path.basename(partner)}>")
            sheet_name = year
            duplicate_worksheet(wb, sheet_name, partner)

        wb = load_workbook(partner)
        wb.active = wb[sheet_name]
        ws = wb.active

        coord = find_cell(ws, "TechCXO")
        partner_name = ws.cell(row=coord[0]+3, column=coord[1]).value
        employee_code = ws.cell(row=coord[0]+4, column=coord[1]).value

        month = int(inputs["year_month"].split("-")[1]) - 1
        coord = find_cell(ws, MONTH[month])
        ws.cell(row=coord[0]-1, column=coord[1]).value = get_adjusted_tenth(inputs["year_month"])

        detail_data = details.loc[partner_name]
        deduction_data = deductions.loc[employee_code]
        if isinstance(deduction_data, Series):
            deduction_data = deduction_data.to_frame().T
        deduction_data = deduction_data.set_index("cdeductcode")

        output_data  = data_to_worksheet(detail_data, deduction_data)
        for i, row in enumerate(range(coord[0]+1, coord[0]+len(output_data)+1)):
            cell = ws.cell(row=row, column=coord[1])
            cell.number_format = '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'
            if cell.value is None or str(cell.value).strip() == "":
                cell.value = output_data[i]
            else:
                cell.value = output_data[i]
                logger.warning("Cell %s is not empty, overwriting value", cell.coordinate)

        wb.save(partner) 

if __name__ == "__main__":
    main()
