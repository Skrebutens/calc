
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
    result = megabit * 8
    return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
    result = (litres * 100)/kilometers
    return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = 0
    result = celsius * 9 / 5 + 32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    a=1
    result = 0
    for i in range(tail)
        result = result + a
        a += 1
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    return str(grams) + "g"
    