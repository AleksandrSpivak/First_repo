from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    congrats = {"Monday": '',
                 "Tuesday": '',
                 "Wednesday": '',
                 "Thursday": '',
                 "Friday": ''
    }

#    today_is = datetime.now().date()
    today_is = datetime(2023, 12, 31).date()
    day_of_week = int(today_is.strftime("%w"))
    next_monday = today_is + timedelta((8 - day_of_week)%7)
    next_friday = next_monday + timedelta(4)
    saturday = next_monday - timedelta(2)
    sunday = next_monday - timedelta(1)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  
        birthday_this_year = birthday.replace(year=today_is.year)

        if (birthday_this_year < today_is) and ((today_is - birthday_this_year).days > 7):
            birthday_this_year = birthday.replace(year=today_is.year + 1)

        if birthday_this_year >= saturday and birthday_this_year <= next_friday:
            if birthday_this_year == saturday or birthday_this_year == sunday or birthday_this_year == next_monday:
                congrats["Monday"] = congrats["Monday"] + name + ', ' 
            if birthday_this_year.strftime("%w") == '2':
                congrats["Tuesday"] = congrats["Tuesday"] + name + ', '
            if birthday_this_year.strftime("%w") == '3':
                congrats["Wednesday"] = congrats["Wednesday"] + name +', '
            if birthday_this_year.strftime("%w") == '4':
                congrats["Thursday"] = congrats["Thursday"] + name + ', '     
            if birthday_this_year.strftime("%w") == '5':
                congrats["Friday"] = congrats["Friday"] + name + ', '    
 
    print(f'Monday: {congrats["Monday"][:-2]}\nTuesday: {congrats["Tuesday"][:-2]}\nWednesday: {congrats["Wednesday"][:-2]}\nThursday: {congrats["Thursday"][:-2]}\nFriday: {congrats["Friday"][:-2]}')

    return congrats



users = [
    {"name": "Billl Gates", "birthday": datetime(1955, 12, 30)},
    {"name": "Bill Gates", "birthday": datetime(1955, 1, 1)},
    {"name": "Bil Gates", "birthday": datetime(1955, 1, 2)},
    {"name": "Bi Gates", "birthday": datetime(1955, 1, 4)},
]

congrats = get_birthdays_per_week(users)
