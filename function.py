from datetime import date, timedelta, datetime


def birthday_list(users: list, date_day) -> list:
    """Функція створеня списку імениників на певний день"""

    result_list = []
    for user in users:
        if (user["birthday"].day == date_day.day) and (user["birthday"].month == date_day.month):
            result_list.append(user["name"])
    return result_list


def get_birthdays_per_week(users: list) -> None:
    """Фцнкція створення імениників на майбутній тиждень"""

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
    for i in range(7):
        period = timedelta(days=i+1)
        birthday_day = period + curr_date  # отримання дати наступного дня
        birthday_weekday = (date_week + i + 1) % 7
        list_b = birthday_list(users, birthday_day)
        print(weekday_name[str(birthday_weekday)], ": ", list_b)
