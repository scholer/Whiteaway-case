# Copyright 2021, Rasmus Sorensen <rasmusscholer@gmail.com>
"""


"""

import pandas as pd


def drop_unwanted_rows(df, report_dict=None, verbose=0):
    if report_dict is None:
        report_dict = {}

    # Remove bad data:
    if verbose:
        print("Rows before QA filtering:", len(df))
    report_dict['nrows_0_input'] = len(df)

    # Remove lines with N/A values:
    df = df_dropna = df.dropna()
    if verbose:
        print("Rows after dropping N/A:", len(df))
    report_dict['nrows_after_dropna'] = len(df)

    # Remove rows with empty columns.
    # This is to ensure that all the rows we are working with has the required fields,
    # e.g. doesn't have empty CustomerID.
    # Strictly, this is only needed for some of the columns.
    # print("Columns with empty values:")
    for column in df.columns:
        df = df[~(df[column] == '')]
    if verbose:
        print("Rows after dropping rows with empty values:", len(df))
    report_dict['nrows_after_dropping_empty'] = len(df)

    # Remove lines that does not represent an actual product:
    # print("Non-product stock codes:")
    non_product_stock_codes = ['BANK CHARGES', 'C2', 'CRUK', 'D', 'DOT', 'M', 'PADS', 'POST']
    df = df[~df['StockCode'].isin(['BANK CHARGES', 'C2', 'CRUK', 'D', 'DOT', 'M', 'PADS', 'POST'])]

    if verbose:
        print("Rows after dropping non-product lines:", len(df))
    if verbose:
        print("Rows after QA filtering:", len(df))
    report_dict['nrows_after_dropping_nonproduct_rows'] = len(df)

    return df


def load_and_filter(filename, report_dict=None, encoding='latin-1', verbose=0):
    """
    For this dataset, I sometimes have issues with UnicodeEncodingErrors, so using Latin-1 encoding.
    (One computer had no issues, the other required encoding='latin-1' to read the data.)

    """
    # Load data
    df = pd.read_csv(filename, keep_default_na=False, encoding=encoding)
    # Remove bad/unwanted rows:
    df = drop_unwanted_rows(df, report_dict=report_dict, verbose=verbose)
    return df




