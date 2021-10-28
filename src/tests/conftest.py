"""
TODO Add module docstring
"""
import logging

import pytest

from src.churn_library import import_data

BANK_DATA_PATH = "./data/bank_data.csv"

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def pytest_configure(config):
    """Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        config.option.log_file = "logs/log.churn_library.log"


@pytest.fixture(scope="module")
def churn_df():
    """Fixture for importing the bank data"""
    try:
        dataframe = import_data(BANK_DATA_PATH)
        logging.info("Testing import_data: SUCCESS")

        yield dataframe

    except FileNotFoundError as err:
        logging.error("Testing import_data: The file wasn't found")
        raise err
