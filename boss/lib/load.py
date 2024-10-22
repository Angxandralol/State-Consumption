from pandas import DataFrame
from os import getenv
from dotenv import load_dotenv
from common import FileController, filename as FILE

load_dotenv(override=True)

REPORT_BOSS = getenv("REPORTBOSS_PATH")

def load_report_boss() -> DataFrame:
    """Load the boss report to get the dataframe."""
    try:
        if ".xlsx" in REPORT_BOSS:
            df = FileController.read_excel(REPORT_BOSS)
            if df.empty:
                raise Exception("Report boss data not found")
            return df
        else:
            raise Exception("Report boss file not found")
    except Exception as error:
        raise error


def save_data_clients(data: DataFrame) -> None:
    try:
        FileController.write_excel(data, filename=FILE.CLIENTS_BY_BRAS)
    except Exception as error:
        raise error


def save_new_report_boss(data: DataFrame) -> None:
    try:
        FileController.write_excel(data, filename=FILE.NEW_REPORT_BOSS)
    except Exception as error:
        raise error


def save_data_porcentage(data: DataFrame) -> None:
    try:
        FileController.write_excel(data, filename=FILE.PORCENTAGE)
    except Exception as error:
        raise error
