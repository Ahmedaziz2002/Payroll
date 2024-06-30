def details():
    name = input("Enter employee name: ")
    employee_number = input("Enter employee number: ")
    department = input("Enter employee department: ")
    basic_salary = float(input("Enter employee basic salary: "))
    allowance = float(input("Enter employee allowances: "))

    print("The employee details are as follows:\n")
    print(f"Employee name is: {name}")
    print(f"Employee number is: {employee_number}")
    print(f"Employee department is: {department}")
    print(f"Employee basic salary is: ${basic_salary}")
    print(f"Employee allowances are: ${allowance}")

    return basic_salary, allowance

def salary(basic_salary, allowance):
    gross_salary = basic_salary + allowance
    print(f"Employee gross salary is: ${gross_salary}")
    return gross_salary

def houselevy(gross_salary):
    house_levy = 1.5 * gross_salary / 100
    print(f"House levy is: ${house_levy}")
    return house_levy

def nssftax(gross_salary):
    nssf = 2.5 * gross_salary / 100
    print(f"NSSF tax is: ${nssf}")
    return nssf

def payetax(gross_salary):
    paye = 6 * gross_salary / 100
    print(f"Employee PAYE is: ${paye}")
    return paye

def net_salary(gross_salary, house_levy, nssf, paye):
    net_salary = gross_salary - (house_levy + nssf + paye)
    print(f"Employee's net income is: ${net_salary}")
    return net_salary

def main():
    while True:
        print("What do you want to do?\n")
        print("1. Get employee details")
        print("2. Compute gross salary")
        print("3. Compute house levy")
        print("4. Compute NSSF tax")
        print("5. Compute PAYE tax")
        print("6. Compute net salary")
        print("7. Exit")

        option = input("> ")

        if option == "1":
            basic_salary, allowance = details()

        elif option == "2":
            try:
                gross_salary = salary(basic_salary, allowance)
            except NameError:
                print("Please get the employee details first (option 1).")

        elif option == "3":
            try:
                house_levy = houselevy(gross_salary)
            except NameError:
                print("Please compute the gross salary first (option 2).")

        elif option == "4":
            try:
                nssf = nssftax(gross_salary)
            except NameError:
                print("Please compute the gross salary first (option 2).")

        elif option == "5":
            try:
                paye = payetax(gross_salary)
            except NameError:
                print("Please compute the gross salary first (option 2).")

        elif option == "6":
            try:
                net_salary(gross_salary, house_levy, nssf, paye)
            except NameError:
                print("Please compute the gross salary, house levy, NSSF tax, and PAYE tax first (options 2-5).")

        elif option == "7":
            print("Exiting the terminal now...")
            break

if __name__ == "__main__":
    main()
