from people import get_employees
from salary import calculate_salary
from datetime import datetime


def datetime_now():
    print(datetime.now())


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    datetime_now()
