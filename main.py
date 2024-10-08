class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_emp_details(self):
        print(f"{self.emp_id} {self.emp_name} {self.emp_salary} {self.emp_department}")

    def calculate_emp_salary(self, salary, hour_worked):
        total = salary
        overtime_amount = 0
        if hour_worked > 50:
            overtime = hour_worked - 50
            overtime_amount = overtime * (salary / 50)
        total += overtime_amount
        self.emp_salary = total
