"""
TODO Add module docstring
"""
import logging

import pytest

from src.data.import_data import import_data
from tests.test_constants import SAMPLE_BANKING_DATA

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


@pytest.fixture()
def raw_data_file(tmpdir):
    """Fixture for creating a temporary data file"""
    file = tmpdir.join("bank_data.csv")

    write_banking_data(file)

    logging.info("raw_data_file: created raw data file @ %s", file)

    yield file


def write_banking_data(file):
    """Write sample banking data to given file path"""
    with open(file, "w") as writer:
        for row in SAMPLE_BANKING_DATA:
            writer.write(row)
            writer.write("\n")
