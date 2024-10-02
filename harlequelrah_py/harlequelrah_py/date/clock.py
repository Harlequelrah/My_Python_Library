from datetime import datetime
from dateutil.relativedelta import relativedelta


def is_bisectile(year):
    if year.isdigit():
        year = int(year)
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def interval(
    birthday_year: int, birthday_month: int, birthday_day: int, type: str = None
):
    birthday_date = datetime(birthday_year, birthday_month, birthday_day)
    today = datetime.today()
    interval = relativedelta(today, birthday_date)
    match type:
        case "year" | "y" | "YEAR":
            return interval.years
        case "month" | "MONTH" | "m":
            return interval.years * 12 + interval.months
        case "day" | "DAY" | "d":
            return (today - birthday_date).days
        case default:
            return None


print(interval(2004, 4, 10, "m"))
