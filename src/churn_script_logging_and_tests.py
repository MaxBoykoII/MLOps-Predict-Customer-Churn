"""
TODO - Add module docstring
"""
import logging

logging.basicConfig(
    filename="./logs/churn_library.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)


def test_import(import_data):
    """
    test data import
    """
    try:
        churn_df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err

    try:
        assert churn_df.shape[0] > 0
        assert churn_df.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows/columns"
        )
        raise err


def test_eda():
    """
    test perform eda function
    """


def test_encoder_helper():
    """
    test encoder helper
    """


def test_perform_feature_engineering():
    """
    test perform_feature_engineering
    """


def test_train_models():
    """
    test train_models
    """
