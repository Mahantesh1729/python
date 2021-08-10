from time import time


def main():
    sec = time()
    years, months, days = cal(sec)
    print(f"Time passed since UNIX epoch:\ntotal years : total months : total days")
    display(years, months, days)
    print("Todays date:")
    display(1970+years, months + 1, days + 1)
    
def cal(sec):
    days = sec // 86400
    years = days // 365
    remdays = days % 365
    months = remdays // 30
    remdays = remdays % 30
    return int(years), int(months), int(remdays)

def display(years, months, days):
    print(f"{years}:{months}:{days}")


main()
