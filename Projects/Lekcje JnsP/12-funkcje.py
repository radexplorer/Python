countries_inf = {}
countries_inf["Polska"] = ("Warszawa", 23.23)
countries_inf["Niemcy"] = ("Berlin", 82.23)
countries_inf["Hiszpania"] = ("Madryt", 45.23)


def show_country_info(country):
    country_inf = countries_inf.get(country)
    print()
    print(country)
    print("--------------")
    print("Stolica: " + country_inf[0])
    print("Liczba miszkańców: " + str(country_inf[1]))


for country in countries_inf.keys():
    print(country)

    # country = input("which country inf do you want display about: ")

    # coontry_inf = countries_inf.get(country)
    # print()
    # print(country)
    # print("--------------")
    # print("Stolica: " + coontry_inf[0])
    # print("Liczba miszkańców: " + str(coontry_inf[1]))

show_country_info("Polska")

###############################################################################################


def dispaly_sum(a, b):
    print(a+b)
    return a+b


dispaly_sum(4, 4)


def calculate_sum(a, b):
    return a+b


sum = calculate_sum(3, 8)
print(sum)

dispaly_sum(234, 785)
