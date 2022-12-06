from datetime import date
import function


# ------------------------------Отримання даних колег із файлу source.txt-------------------
users_list = []
with open("source.txt", "r") as fh:
    while True:
        users_list.append(fh.readline())
        if users_list[-1] == "":
            break
users_list.remove("")
# --------------------------Формування списку колег-------------------------------------
users_list_dict = []
for u in users_list:
    l = u.split(" ")
    k = l[1].split("-")
    d = {"name": l[0], "birthday": date(
        year=int(k[0]), month=int(k[1]), day=int(k[2].removesuffix("\n")))}
    users_list_dict.append(d)

function.get_birthdays_per_week(users_list_dict)
