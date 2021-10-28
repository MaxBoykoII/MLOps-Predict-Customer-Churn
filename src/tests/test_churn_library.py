"""
TODO - Add module docstring
"""
import logging


def test_import(churn_df):
    """
    test data import
    """
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
