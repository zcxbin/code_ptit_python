from datetime import datetime

class Person:
    def __init__(self, code, name, time_in, time_out) -> None:
        self.code = code
        self.name = name
        self.time = abs(datetime.strptime(time_out, '%H:%M') - datetime.strptime(time_in, '%H:%M'))

people = []
for _ in range(int(input())):
    people.append(Person(input(), input(), input(), input()))

people.sort(key=lambda person: -person.time.total_seconds())

for person in people:
    hours = person.time.seconds // 3600
    minutes = (person.time.seconds // 60) % 60
    print(person.code, person.name, hours, 'gio', minutes, 'phut')


'''
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
'''