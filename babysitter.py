# starts no earlier than 5:00PM
# leaves no later than 4:00AM
# only babysits for one family per night
# gets paid for full hours (no fractional hours)
# should be prevented from mistakes when entering times (e.g. end time before start time, or outside of allowable work hours)
# The job:

# Pays different rates for each family (based on bedtimes, kids and pets, etc...)
# Family A pays $15 per hour before 11pm, and $20 per hour the rest of the night
# Family B pays $12 per hour before 10pm, $8 between 10 and 12, and $16 the rest of the night
# Family C pays $21 per hour before 9pm, then $15 the rest of the night
# The time ranges are the same as the babysitter (5pm through 4am)

def hours_worked(start_time, end_time):
    if start_time > end_time:
        raise Exception("shift end time is before start time")

    start_time = _check_start_time(start_time)
    end_time = _check_end_time(end_time)
    total_hours = (end_time - start_time)
    return total_hours

def _check_end_time(end_time):
    if end_time > 4 and end_time in range(0,12 + 1):
        end_time = 4
    # if end_time in range(0,12 + 1):
    #     end_time += 24
    return end_time

def _check_start_time(start_time):
    if start_time < 17 and start_time not in range(0, 12 + 1):
        start_time = 17
    return start_time

# def check_start_time(start_time):
#     if start_time < 17:
#         start_time = 17
#     return start_time

# def check_end_time(end_time):
#     if end_time not in range(12,24 + 1):
#         end_time += 24
#     return end_time

# def hours_worked():
#     total_hours = (end-time - start_time)
#         # return start_time



# def hours_worked(start_time, end_time):
#     if check_start_time(start_time):
#         start_time = 17
#         # return start_time

#     elif check_end_time(end_time)
#          end_time += 24
#         #  return end_time

#     else:
#         pass

#     total_hours = end_time - start_time
#     return total_hours


# def check_start_time(start_time):
#     return start_time < 17
#     #     start_time = 17
#     # return start_time
# def check_end_time(end_time):
#     return end_time not in range(12,24 + 1)
#     #     end_time += 24
#     # return end_time

# def calc_basic_pay(start_time, end_time):
#     check_start_time(start_time):
#     check_end_time(end_time):

#     work_time = (end_time - start_time)
#     sample_pay_rate = 10
#     pay = (work_time * sample_pay_rate)
