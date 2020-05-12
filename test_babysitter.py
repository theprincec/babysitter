from babysitter import *

def test_hours_worked():
    assert hours_worked(17,18) == 1

def test_accurate_start_time():
    assert hours_worked(16,18) == 1

def test_accurate_end_time():
    assert hours_worked(23,0) == 1  