def pass_count(PeopleDictionary):
    count = 0
    for grade in PeopleDictionary.values():
        if grade >= 80:
            count += 1
    return count

grade = {
    "Alice": 85,
    "Bob": 90,
    "Eve": 70,
    "Acie": 80,
}


print(pass_count(grade))


