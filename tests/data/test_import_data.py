"""TODO"""
import logging

from src.data.import_data import import_data


def test_import_data(raw_data_file):
    """
    test data import
    """
    churn_df = import_data(raw_data_file)

    assert churn_df.shape[0] > 0, "number of rows was zero, should be greater than zero"
    assert (
        churn_df.shape[1] > 0
    ), "number of columns was zero, should be greater than zero"

    logging.info("Testing import_data: The file has both rows and columns")
