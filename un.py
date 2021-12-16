"""Xmas project./ Leet codes"""

# Project 1 -- Planner
import datetime

TIME: float = 24.0

username: str = input("What is your name? ")

dict_of_things: dict[str, float] = {}
time_dict: dict[str, str] = {}


date = datetime.datetime.now()

def am_pm(a: dict[str, float], b: str) -> str:
    for key in a:
        total_time: float = 0.0
        total_time += a[key]
        if key == b:
            break
    if total_time < 12:
        return "am"
    else:
        return "pm"




def time(a: dict[str, str]) -> None:
    for key in a:
        a[key] = a[key][0] + am_pm(dict_of_things, key) + " - " + a[key][2] + am_pm(dict_of_things, key)



def total(a: dict[str, float]) -> float:
    total: float = 0.0
    for key in a:
        total += a[key]
    return total


def convert(a: dict[str, float], b: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for key in a:
        if b == "hours":
            result[key] = str(a[key]) + " hours"
        else:
            result[key] = str(a[key] * 60) + " minutes"
    return result


def days() -> str:
    if str(date.day)[len(str((date.day))) - 1] == '1':
        return "st"
    elif str(date.day)[len(str((date.day))) - 1] == '2':
        return "nd"
    elif str(date.day)[len(str((date.day))) - 1] == '3':
        return 'rd'
    else:
        return 'th'




while total(dict_of_things) < TIME:
    if total(dict_of_things) > 24:
        break
    thing: str = input("What do you need to do? ")
    length: float = float(input("How long will it take? "))
    print("Enter in 'A-B' format where A = the start and B = the end")
    time_of_day: str = input("When do you want to do this? ")
    dict_of_things[thing] = length
    time_dict[thing] = time_of_day


pref: str = input("Do you want your results in hours or minutes? ")

new_dict: dict[str, str] = convert(dict_of_things, pref)

new_day: str = date.strftime("%A")
new_month: str = date.strftime("%B")
print(f"{username}, you have a full day of: {new_dict} on {new_day}, {new_month} {date.day}{days()}, {date.year}.")
print(time_dict)
 
# Ideas - add 24 hour schedule (ie 12am - 8am), Learn flask, make this into a website
