"""
    library file
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_name = "StudentPerformanceFactors.csv"


def load_dataset():
    df = pd.read_csv(dataset_name)
    return df


def get_mean(df, col):
    return df[col].mean()


def get_median(df, col):
    return df[col].median()


def get_standardDev(df, col):
    return df[col].std()


def create_histogram(df, col="Exam_Score"):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col].dropna(), bins=30, kde=True)
    plt.title("Histogram of " + col)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()


def create_scatter(data, x_col, y_col):
    data.plot.scatter(x=x_col, y=y_col)
    plt.title(x_col + " vs. " + y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
