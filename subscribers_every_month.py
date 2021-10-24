def make_list_good(input: list) -> list:
    return [entry[1] for entry in input]

# figures out Youtube subs every month
# from the current month (end_date) to the first month given on SocialBlade
# using the sub_list from the source code on SocialBlade
# outputting a dictionary of subscribers and times
def subscribers_every_month(end_date: tuple, sub_list: list, sub_dict=dict()) -> dict:
    month_list = ['Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan']
    month_number = month_list.index(end_date[0])
    year_number = int(end_date[1])
    for sub in sub_list:
        date_string = f'{month_list[month_number]} {year_number}'
        if date_string not in sub_dict:
            sub_dict[date_string] = []
        sub_dict[date_string].append(sub)
        if month_number == 11:
            month_number = 0
            year_number -= 1
        else:
            month_number += 1
    return sub_dict
