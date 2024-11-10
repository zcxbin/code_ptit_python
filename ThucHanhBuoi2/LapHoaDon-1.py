class Customer:
    def __init__(self, index, name, previous_reading, after_reading) -> None:
        self.code = f'KH{str(index).zfill(2)}'
        self.name = name
        consumption = after_reading - previous_reading
        if consumption > 100:
            self.bill = ((consumption - 100) * 200 + 50 * (100 + 150)) * 1.05
        elif consumption > 50:
            self.bill = ((consumption - 50) * 150 + 50 * 100) * 1.03
        else:
            self.bill = consumption * 100 * 1.02

customers = []
for t in range(int(input())):
    name = input()
    previous_reading = int(input())
    after_reading = int(input())
    customers.append(Customer(t + 1, name, previous_reading, after_reading))

customers.sort(key=lambda customer: (-customer.bill, customer.code))

for customer in customers:
    print(customer.code, customer.name, f'{customer.bill:.0f}')


'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''