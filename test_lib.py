"""
Test goes here
"""

from mylib.calculator import load_dataset, get_mean, get_median, get_standardDev


def test_load_dataset():
    student_data = load_dataset()
    assert student_data is not None
    assert student_data.shape == (6607, 20)


def test_summary_stats():
    student_data = load_dataset()
    col = "Exam_Score"
    compare_col = "Hours_Studied"
    test_mean = get_mean(student_data, col)
    test_median = get_median(student_data, col)
    test_std = get_standardDev(student_data, col)
    describe_test = student_data.describe()
    assert describe_test.loc["mean", "Exam_Score"] == test_mean
    assert describe_test.loc["50%", "Exam_Score"] == test_median
    assert describe_test.loc["std", "Exam_Score"] == test_std


if __name__ == "__main__":
    test_load_dataset()
    test_summary_stats()
