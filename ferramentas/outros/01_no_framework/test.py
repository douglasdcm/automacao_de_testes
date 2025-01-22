from src import sum


def test_sum_two_numbers():
    # arrange
    data_table = [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 0, -1),
    ]
    for data in data_table:
        x = data[0]
        y = data[1]
        expected = data[2]

        # act
        actual = sum(x, y)

        # assert
        _assert(
            test_sum_1_and_0_returns_1,
            actual,
            expected,
        )


def test_sum_1_and_0_returns_1():
    # arrange
    x = 1
    y = 0
    expected = 1

    # act
    actual = sum(x, y)

    # assert
    _assert(
        test_sum_1_and_0_returns_1,
        actual,
        expected,
    )


def test_sum_1_and_3_returns_4():
    # arrange
    x = 1
    y = 3
    expected = 4

    # act
    actual = sum(x, y)

    # assert
    _assert(
        test_sum_1_and_3_returns_4,
        actual,
        expected,
    )


def _assert(
    function,
    actual,
    expected,
):
    if actual != expected:
        print(
            f"FAILED '{function.__name__}'. Expected '{expected}', returned '{actual}'"
        )
    else:
        print(f"PASSED '{function.__name__}'")


if __name__ == "__main__":
    test_sum_1_and_3_returns_4()
    test_sum_1_and_0_returns_1()
    test_sum_two_numbers()
