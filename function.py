from datetime import date, timedelta, datetime


def birthday_list(users: list, date_day) -> list:
    """Функція створеня списку імениників на певний день"""

    result_list = []
    for user in users:
        if (user["birthday"].day == date_day.day) and (user["birthday"].month == date_day.month):
            result_list.append(user["name"])
    return result_list


def get_birthdays_per_week(users: list) -> None:
    """Функція створення імениників на майбутній тиждень"""

    weekday_name = {
        "0": "Monday",
        "1": "Tuesday",
        "2": "Wednesday",
        "3": "Thursday",
        "4": "Friday",
        "5": "Saturday",
        "6": "Sunday"
    }
    curr_date = date.today()
    date_week = curr_date.weekday()
    week_delta = 5 - date_week
    weekday_list = []
    for i in range(7):
        period = timedelta(days=i + week_delta)
        birthday_day = period + curr_date  # отримання дати дня народження
        birthday_weekday = (date_week + i + week_delta) % 7
        list_b = birthday_list(users, birthday_day)
        if (birthday_weekday == 5) or (birthday_weekday == 6):
            weekday_list.extend(list_b)
        if birthday_weekday == 0:
            weekday_list.extend(list_b)
            print(weekday_name[str(birthday_weekday)],
                  " (with Saturday and Sunday): ", weekday_list)
        elif (birthday_weekday < 5) and (birthday_weekday > 0):
            print(weekday_name[str(birthday_weekday)], " : ", list_b)
