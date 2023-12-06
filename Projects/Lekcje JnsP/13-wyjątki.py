countries_and_capitals = {"Poland": "Warssaw",
                          "Czechia": "Prague",
                          "Germany": "Berlin"}

try:
    print(2/7)
    print(countries_and_capitals["USA"])
except KeyError:
    print("klucz nie został znaleziony")
except ZeroDivisionError:
    print("Nie dziel przez zero")
finally:
    print("To wykona się zawsze")

print("WyJąTeK")


