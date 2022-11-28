def study_schedule(permanence_period, target_time):
    if type(target_time) is not int or permanence_period is None:
        return None
    times = 0
    for time in permanence_period:
        if type(time[0]) is not int or type(time[1]) is not int:
            return None
        if time[0] <= target_time and time[1] >= target_time:
            times += 1
    return times
