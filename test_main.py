"""
Test goes here

"""

from main import get_describe, col_summ_stats


def test_get_describe():
    test_describe = get_describe()
    assert test_describe.shape == (8, 7)


def test_col_summ_stats():
    col = "Exam_Score"
    student_data_describe = get_describe()
    summ_stats_dictionary = col_summ_stats(col)
    assert (
        student_data_describe.loc["mean", "Exam_Score"] == summ_stats_dictionary["mean"]
    )
    assert (
        student_data_describe.loc["50%", "Exam_Score"]
        == summ_stats_dictionary["median"]
    )
    assert (
        student_data_describe.loc["std", "Exam_Score"] == summ_stats_dictionary["std"]
    )


if __name__ == "__main__":
    test_get_describe()
    test_col_summ_stats()
