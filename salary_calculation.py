
def calculate_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    pf = basic_salary * 0.12

    gross_salary = basic_salary + hra + da
    net_salary = gross_salary - pf

    print("\nSalary Details")
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("PF:", pf)
    print("Gross Salary:", gross_salary)
    print("Net Salary:", net_salary)

calculate_salary(30000)
