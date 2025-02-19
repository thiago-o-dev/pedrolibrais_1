class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"

def add_employee(employees):
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")
    employee = Employee(name, age, position)
    employees.append(employee)
    save_employees(employees)

def save_employees(employees):
    with open("employees.txt", "w") as file:
        for employee in employees:
            file.write(f"{employee.name},{employee.age},{employee.position}\n")

def load_employees():
    employees = []
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                name, age, position = line.strip().split(",")
                employees.append(Employee(name, age, position))
    except FileNotFoundError:
        pass
    return employees

def list_employees(employees):
    for employee in employees:
        print(employee)

def main():
    employees = load_employees()
    while True:
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            list_employees(employees)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()