def add_time(start, duration, starting_day=None):
    start = start.replace(':', ' ')
    s_splited = start.split(' ')
    start_data = list()
    for data in s_splited:
        try:
            start_data.append(int(data))
        except:
            break

    duration_data = list()
    duration = duration.split(':')
    for data in duration:
        duration_data.append(int(data))

    if s_splited[2] == 'PM':
        s_hour = start_data[0] + 12
    else:
        s_hour = start_data[0]
    s_minute = start_data[1]
    d_hour = duration_data[0]
    d_minute = duration_data[1]

    # Minutes
    minutes = s_minute + d_minute
    if minutes >= 60:
        m = minutes - 60
        additional_h = 1
    else:
        m = minutes
        additional_h = 0

    if len(str(m)) == 1:
        m = f"0{m}"

    # Hours
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