from typing import List
from pandera.errors import SchemaErrors
from app.schema import DetailsSchema, DeductionReportSchema
from pandas import DataFrame, read_excel, MultiIndex, to_numeric
from logging import basicConfig, getLogger, INFO


logger = getLogger(__name__)
basicConfig(
    level=INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


def import_details_table(src_path: str) -> DataFrame:
    df = read_excel(
        src_path,
        skiprows=1,
        sheet_name="Details",
        header=None
    )
    df = df.iloc[:, 0:23]
    non_empty = df.dropna(subset=[0]) # Drop rows where the first column is NaN
    non_empty = non_empty.set_index(0)
    non_empty = non_empty.fillna("")
    new_header = MultiIndex.from_arrays([
        non_empty.iloc[0].str.strip().values,
        non_empty.iloc[1].str.strip().values
        ])
    non_empty.columns = new_header
    non_empty = non_empty.iloc[2:]  # Skip the first two rows
    non_empty = non_empty.apply(to_numeric, errors='coerce')  # Converts non-numeric to NaN

    return non_empty

def import_deduction_report_table(src_path: str) -> DataFrame:
    columns = [
        "ceecode",
        "namount",
        "cdeductcode"
    ]
    df = read_excel(src_path, sheet_name="Deduction Report",usecols=columns)
    df = df.dropna(how="any")

    return df


def import_tables(src_path: str) -> List[DataFrame]:
    details = import_details_table(src_path)
    try:
        validated_details = DetailsSchema.validate(details)
    except SchemaErrors as e:
        logger.error("Validation error summary:")
        logger.error(e.failure_cases)  # This gives a DataFrame of failed cases
    except Exception as e:
        logger.error("An unexpected error occurred during validation.")
        logger.error(str(e))

    deductions = import_deduction_report_table(src_path)
    try:
        validated_deductions = DeductionReportSchema.validate(deductions)
    except SchemaErrors as e:
        logger.error("Validation error summary:")
        logger.error(e.failure_cases)  # This gives a DataFrame of failed cases
    except Exception as e:
        logger.error("An unexpected error occurred during validation.")
        logger.error(str(e))
    
    return (validated_details, validated_deductions)
