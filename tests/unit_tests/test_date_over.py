import server


def test_date_over_success():
    date_string_after_today = "2077-10-23 09:13:00"
    assert server.date_over(date_string_after_today) is True


def test_date_over_fail():
    date_string_after_today = "1970-01-01 00:00:00"
    assert server.date_over(date_string_after_today) is False
