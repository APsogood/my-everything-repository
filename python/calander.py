def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        return 31

def display_calendar(year, month):
    print("\n" + f"{' ' * 10}{month}/{year}" + "\n")
    print("Mo Tu We Th Fr Sa Su")
    weekday = (1 + (13 * (month + 1)) // 5 + year + (year // 4) - (year // 100) + (year // 400)) % 7
    print("   " * weekday, end="")
    for day in range(1, get_days_in_month(year, month) + 1):
        print(f"{day:2} ", end="")
        if (day + weekday) % 7 == 0:
            print()
    print("\n")

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    display_calendar(year, month)

if __name__ == "__main__":
    main()

