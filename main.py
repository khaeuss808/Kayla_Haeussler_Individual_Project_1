"""
Main cli or app entry point
"""

from mylib.calculator import (
    load_dataset,
    get_mean,
    get_median,
    get_standardDev,
    create_histogram,
    create_scatter,
)


def get_describe():
    data = load_dataset()
    return data.describe()


def col_summ_stats(col):
    data = load_dataset()
    mean = get_mean(data, col)
    median = get_median(data, col)
    std = get_standardDev(data, col)
    print(f"Column of Interest: {col}")
    print(f"Mean: {mean: .2f}")
    print(f"Median: {median: .2f}")
    print(f"Standard Deviation: {std: .2f}")
    return {"mean": mean, "median": median, "std": std}


def generate_visualization(col, col2):
    data = load_dataset()
    create_histogram(data, col)
    create_scatter(data, col, col2)


def save_to_md():
    with open("test.md", "a") as file:
        file.write("test")


if __name__ == "__main__":
    print(get_describe())
    col_of_intrst = "Exam_Score"
    compare_col = "Hours_Studied"
    col_summ_stats(col_of_intrst)
    generate_visualization(col_of_intrst, compare_col)
