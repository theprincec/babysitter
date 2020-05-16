from babysitter import *
import pytest

def test_hours_worked():
    assert hours_worked(17,18) == 1

def test_accurate_start_time():
    assert hours_worked(16,18) == 1

def test_accurate_end_time():
    assert hours_worked(3,5) == 1

def test_exceptions_for_start_and_end_time():
    with pytest.raises(Exception) as err:
        start_time = 18
        end_time = 17
        assert hours_worked(start_time,end_time)
    err.match("shift end time is before start time")

def test_end_time_after_midnight():
    assert hours_worked(0,5) == 4