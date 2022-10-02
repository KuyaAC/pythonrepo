def online_count(PeopleDictionary):
    count = 0
    for status in PeopleDictionary.values():
        if status == 'online':
            count += 1
    return count

status = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


print(online_count(status))

