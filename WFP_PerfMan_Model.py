# Define the employee class to store data
class Employee:
    def __init__(self, name, performance_score, development_score, leadership_score):
        self.name = name
        self.performance_score = performance_score
        self.development_score = development_score
        self.leadership_score = leadership_score

    def total_score(self):
        return self.performance_score + self.development_score + self.leadership_score

    def __repr__(self):
        return f"{self.name}: Performance={self.performance_score}, Development={self.development_score}, Leadership={self.leadership_score}, Total={self.total_score()}"


# Create a function to add employee data
def add_employee(employees):
    name = input("Enter employee's name: ")
    performance_score = float(input("Enter performance score (0-10): "))
    development_score = float(input("Enter development score (0-10): "))
    leadership_score = float(input("Enter leadership score (0-10): "))

    new_employee = Employee(name, performance_score, development_score, leadership_score)
    employees.append(new_employee)
    print(f"Employee {name} added successfully!\n")


# Create a function to display all employees
def display_employees(employees):
    if not employees:
        print("No employees to display.")
    else:
        for employee in employees:
            print(employee)
    print("\n")


# Create a function to generate a report of top performers
def generate_top_performers_report(employees):
    if not employees:
        print("No employees available for the report.")
    else:
        sorted_employees = sorted(employees, key=lambda e: e.total_score(), reverse=True)
        print("Top Performers (sorted by total score):")
        for employee in sorted_employees:
            print(employee)
    print("\n")


# Create a function to update employee data
def update_employee(employees):
    name = input("Enter the name of the employee to update: ")
    employee = next((e for e in employees if e.name == name), None)

    if employee:
        print(f"Updating data for {employee.name}. Current scores - Performance: {employee.performance_score}, Development: {employee.development_score}, Leadership: {employee.leadership_score}")
        employee.performance_score = float(input("Enter new performance score (0-10): "))
        employee.development_score = float(input("Enter new development score (0-10): "))
        employee.leadership_score = float(input("Enter new leadership score (0-10): "))
        print(f"Updated scores for {employee.name}.\n")
    else:
        print(f"Employee {name} not found.\n")


# Main loop for the script
def main():
    employees = []
    while True:
        print("Employee Performance and Leadership Tracking System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Generate Top Performers Report")
        print("4. Update Employee Data")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            generate_top_performers_report(employees)
        elif choice == '4':
            update_employee(employees)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
