"""
Module Docstring - TODO
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()

DEFAULT_PLOT_SIZE = (20, 10)


def import_data(pth):
    """
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    """
    return pd.read_csv(pth)


def perform_eda(churn_df):
    """
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    """
    save_churn_plot(churn_df)
    save_marital_status_plot(churn_df)
    save_total_trans_ct_plot(churn_df)
    save_heatmap_plot(churn_df)


def save_heatmap_plot(churn_df):
    """Saves a heatmap plot based on the columns in the churn dataframe"""
    plt.figure(figsize=DEFAULT_PLOT_SIZE)
    sns.heatmap(churn_df.corr(), annot=False, cmap="Dark2_r", linewidths=2)
    plt.show()


def save_total_trans_ct_plot(churn_df):
    """Saves a distplot based on the Total_Trans_Ct column"""
    plt.figure(figsize=DEFAULT_PLOT_SIZE)
    sns.distplot(churn_df["Total_Trans_Ct"])


def save_marital_status_plot(churn_df):
    """Saves a bar plot based on the Marital_Status column"""
    plt.figure(figsize=DEFAULT_PLOT_SIZE)
    churn_df.Marital_Status.value_counts("normalize").plot(kind="bar")


def save_churn_plot(churn_df):
    """Saves a histogram plot based on a derived churn column"""
    churn = calculate_churn(churn_df)
    plt.figure(figsize=DEFAULT_PLOT_SIZE)
    churn.hist()


def calculate_churn(churn_df):
    """Calculates customer churn based on the Attrition_Flag column"""
    return churn_df["Attrition_Flag"].apply(
        lambda val: 0 if val == "Existing Customer" else 1
    )


def encoder_helper(churn_df, category_lst, response):
    """
    helper function to turn each categorical column into a new column with
    propotion of churn for each category - associated with
    cell 15 from the notebook

    input:
        df: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name
                      [optional argument that could be used
                      for naming variables or index y column]

    output:
            df: pandas dataframe with new columns for
    """
    print(churn_df, category_lst, response)


def perform_feature_engineering(churn_df, response):
    """
    input:
        df: pandas dataframe
        response: string of response name
                  [optional argument that could be used for naming variables
                   or index y column]

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    """
    print(churn_df, response)


def classification_report_image():
    """
    produces classification report for training and testing results
    and stores report as image in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds_lr: training predictions from logistic regression
            y_train_preds_rf: training predictions from random forest
            y_test_preds_lr: test predictions from logistic regression
            y_test_preds_rf: test predictions from random forest

    output:
             None
    """


def feature_importance_plot():
    """
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            X_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    """


def train_models():
    """
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    """
