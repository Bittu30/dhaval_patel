def city_checker():
    usa = ['atlanta', 'new york', 'chicago', 'baltimore']
    uk = ['london', 'bristol', 'cambridge']
    india = ['mumbai', 'delhi', 'bangalore']

    city = input("enter city name: ")

    if city in usa:
        print(city, " is in usa")
    elif city in uk:
        print(city, "is in uk")
    elif city in india:
        print(city, 'is in india')
    else:
        print("I won't be able to tell you which city")


def city_country_checker():
    usa = ['atlanta', 'new york', 'chicago', 'baltimore']
    uk = ['london', 'bristol', 'cambridge']
    india = ['mumbai', 'delhi', 'bangalore']

    city1 = input("Enter city 1:")
    city2 = input("Enter city 2:")

    if city1 in usa and city2 in usa:
        print("Both cities are in USA")
    elif city1 in uk and city2 in uk:
        print("Both cities are in UK")
    elif city1 in india and city2 in india:
        print("Both cities are in India")
    else:
        print("They dont belong to some country")


city_checker()
city_country_checker()

exp = [2000, 2350, 2600, 2130, 2190]
exp[1] - exp[2]

2000 in exp

exp.append(1980)

exp[3] = exp[3] - 200
