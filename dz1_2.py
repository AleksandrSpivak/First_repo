from datetime import datetime

# input {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}
# temp_dict{'Monday': ['Bill Gates'], 'Thursday': ['Jan Koum']}
# вывод, начиная со следующего дня

def is_weekend(date):
    if date.strftime("%w") == '0' or date.strftime("%w") == '6':
        return True
    else:
        return False

def get_birthdays_per_week(users):
    
    congrats = {"Monday": '',
                 "Tuesday": '',
                 "Wednesday": '',
                 "Thursday": '',
                 "Friday": ''
    }

#    today_is = datetime.now().date()
    today_is = datetime(2023, 12, 22).date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  
        birthday_this_year = birthday.replace(year=today_is.year)

        if int(today_is.strftime("%j")) - int(birthday_this_year.strftime("%j")) > (365 - 7):
            birthday_this_year = birthday.replace(year=today_is.year + 1)

        delta_days = (birthday_this_year - today_is).days
        if delta_days < 7:

            if is_weekend(birthday_this_year) and is_weekend(today_is) and delta_days in [-1, 0, 1]:
                congrats["Monday"] = congrats["Monday"] + name + ', '
            if birthday_this_year.strftime("%w") == '1':
                congrats["Monday"] = congrats["Monday"] + name + ', '            
            if birthday_this_year.strftime("%w") == '2':
                congrats["Tuesday"] = congrats["Tuesday"] + name + ', '
            if birthday_this_year.strftime("%w") == '3':
                congrats["Wednesday"] = congrats["Wednesday"] + name +', '
            if birthday_this_year.strftime("%w") == '4':
                congrats["Thursday"] = congrats["Thursday"] + name + ', '     
            if birthday_this_year.strftime("%w") == '5':
                congrats["Friday"] = congrats["Friday"] + name + ', '

    for key in congrats:
        if len(congrats[key]) > 0:
            congrats[key] = congrats[key][:-2]      
    print(f'Monday: {congrats["Monday"]}\nTuesday: {congrats["Tuesday"]}\nWednesday: {congrats["Wednesday"]}\nThursday: {congrats["Thursday"]}\nFriday: {congrats["Friday"]}')

    return 



users = [
    {"name": "Billl Gates", "birthday": datetime(1955, 12, 30)},
    {"name": "Bill Gates", "birthday": datetime(1955, 12, 31)},
    {"name": "Bil Gates", "birthday": datetime(1955, 1, 2)},
    {"name": "Bi Gates", "birthday": datetime(1955, 1, 4)},
]

congrats = get_birthdays_per_week(users)