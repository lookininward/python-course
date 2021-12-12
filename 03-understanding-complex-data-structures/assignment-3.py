persons = [
    {
        "name": "Michael",
        "age": 30,
        "hobbies": [
            "programming",
            "trail running"
        ]
    },
    {
        "name": "Kiersty",
        "age": 26,
        "hobbies": [
            "sleeping",
            "reading"
        ]
    },
    {
        "name": "Misty",
        "age": 6,
        "hobbies": [
            "eating",
            "eating again"
        ]
    }
]

names = [person["name"] for person in persons]
print(names)

all_older_than_twenty = all([person["age"] > 20 for person in persons])
print(all_older_than_twenty)

copied_persons_list = [person.copy() for person in persons]
copied_persons_list[0]["name"] = "Donkey"

a, b, c = persons
print(a, b, c)
print(persons)
print(copied_persons_list)
