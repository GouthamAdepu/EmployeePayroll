
employees = []

def register_employee(emp_id, name, department, basic_salary):
    if emp_id <= 0 or basic_salary <= 0 or not name.strip():
        print("Invalid employee details")
        return

    for emp in employees:
        if emp["id"] == emp_id:
            print("Employee ID already exists")
            return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "basic_salary": basic_salary
    }

    employees.append(employee)
    print("Employee registered successfully!")

def display_employees():
    print("\nEmployee Details")
    for emp in employees:
        print(emp)

register_employee(101, "Rahul", "IT", 30000)
register_employee(102, "Arjun", "HR", 25000)

display_employees()
