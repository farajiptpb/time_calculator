"""
This app contains a function that gets start time in 12-hours format(ex 12:26 AM) and gets duration
and also starting day(optional) and gives result time in the same format
"""


def add_time(start, duration, starting_day=None):
    # Extract usable data from starting time
    start = start.replace(':', ' ')
    s_splited = start.split(' ')
    start_data = list()
    for data in s_splited:
        try:
            start_data.append(int(data))
        except:
            break

    # Extract usable data from duration time
    duration_data = list()
    duration = duration.split(':')
    for data in duration:
        duration_data.append(int(data))

    # converting 12-hours format to 24-hours format
    if s_splited[2] == 'PM':
        s_hour = start_data[0] + 12
    else:
        s_hour = start_data[0]
    s_minute = start_data[1]
    d_hour = duration_data[0]
    d_minute = duration_data[1]

    # Minutes calculation and adding converting minute to hour when minute >= 60

    minutes = s_minute + d_minute
    if minutes >= 60:
        m = minutes - 60
        additional_h = 1
    else:
        m = minutes
        additional_h = 0

    if len(str(m)) == 1:
        m = f"0{m}"

    # Hours calculation;if hours is more than 24 it goes to next days so n is number of days
    # h is hours of time in that day
    hours = s_hour + d_hour + additional_h
    if hours >= 24:
        h = hours % 24
        n = hours // 24
    else:
        h = hours
        n = 0

    if h >= 12:
        f = 'PM'
        h = h - 12
    else:
        f = 'AM'
        h = h

    if h == 0:
        h = 12

    # about starting day parameter
    week = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    if starting_day == None:
        if n != 0:
            if n == 1:
                return f"{h}:{m} {f} (next day)"
            else:
                return f"{h}:{m} {f} ({n} days later)"
        else:
            return f"{h}:{m} {f}"
    else:
        starting_day = starting_day.lower()
        index = week.index(starting_day)
        new_index = index + n
        if new_index >= 7:
            new_index = new_index % 7
        d = week[new_index]
        d = d.title()
        if n != 0:
            if n == 1:
                return f"{h}:{m} {f}, {d} (next day)"
            else:
                return f"{h}:{m} {f}, {d} ({n} days later)"
        else:
            return f"{h}:{m} {f}, {d}"


a = add_time('11:40 AM', '0:25')

print(a)
