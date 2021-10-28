"""
TODO - Add module docstring
"""
import logging

from src.churn_library import import_data

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def test_import():
    """
    test data import
    """
    try:
        churn_df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_data: The file wasn't found")
        raise err

    assert churn_df.shape[0] > 0, "number of rows was zero, should be greater than zero"
    assert (
        churn_df.shape[1] > 0
    ), "number of columns was zero, should be greater than zero"

    logging.info("Testing import_data: The file has both rows and columns")


# def test_eda():
#     """
#     test perform eda function
#     """


# def test_encoder_helper():
#     """
#     test encoder helper
#     """


# def test_perform_feature_engineering():
#     """
#     test perform_feature_engineering
#     """


# def test_train_models():
#     """
#     test train_models
#     """
