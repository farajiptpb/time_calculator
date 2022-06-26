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

    return start_data, duration_data


a = add_time('4:33 AM', '4:50')

print(a)