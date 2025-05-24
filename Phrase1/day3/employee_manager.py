"""
Add new employee (ID, name, age, department)

View all employees

Search by employee ID

Delete employee by ID

Show employees grouped by department
"""

class EmployeeManager:
    def __init__(self):
        self.emp_detail = dict()

    def add_new_employee(self, id, name, age, department):
        """Adding new employee into the system."""
        if id in self.emp_detail:
            print("Cannot add this ID, please provide different ID.")
            return 
        if id == '' or name == '' or age == '' or department == '' :
            print("please enter all the details to Add.")
            return
        self.emp_detail[id] = {"name":name, "age": age, "dept":department}
        print("Employee Added Successfully.")
    
    def view_all_employee(self):
        """View All Employees in the system."""
        if self.emp_detail == {}:
            print("Add any employee to view.")
            return
        for emp in self.emp_detail:
            print(f"Employee: {emp}; name: {self.emp_detail[emp]['name']}; age: {self.emp_detail[emp]['age']}; dept: {self.emp_detail[emp]['dept']}") 
    def search_by_employee(self, employee):
        """Search Employee based on their ID."""
        if employee in self.emp_detail:
            print(f"Employee {employee} is found in our system: {self.emp_detail[employee]}")
        else:
            print(f"Employee {employee} not found in our system.")
            
    def delete_by_employee(self, employee):
        """Delete particular employee from the system."""
        if employee in self.emp_detail:
            del self.emp_detail[employee]
            print(f"Employee {employee} successfully deleted from the system.")
        else:
            print(f"Employee {employee} doesn't exists.")

    def dept_of_employee(self):
        # grouped_emp_list = []
        dept_map = {}
        for employee in self.emp_detail:
            dept_map.setdefault(self.emp_detail[employee]['dept'],[]).append(self.emp_detail[employee]['name'])

        for dept in dept_map:
            print(f"{dept} - {", ".join(dept_map[dept])}")



def main():
    print("Welcome to Employee Management System.")
    empmaster = EmployeeManager()
    system_start = True
    try: 
        while system_start:
            user_input = input("""please Enter any of the below option: 
        1. Add
        2. View 
        3. Search
        4. Delete
        5. Show
                            
        press Enter to Quit: """)
            
            user_input = user_input.lower().strip()
            if user_input == '' or user_input not in ['add','view','search','delete','show','1','2','3','4','5']:
                system_start = False 
                continue 

            if user_input in ['add', '1']:
                id = input("Please enter the userid: ").strip()
                name = input("Please enter the name: ").strip()
                age = input("Please enter the age: ").strip()
                department = input("Please enter the department: ").strip()
                empmaster.add_new_employee(id, name, age, department)
            
            elif user_input in ['view', '2']:
                empmaster.view_all_employee() 
            
            elif user_input in ['search', '3']:
                employee = input('Enter Employee Number: ')
                empmaster.search_by_employee(employee)
            
            elif user_input in ['delete', '4']:
                employee = input('Enter the Employee to delete: ')
                empmaster.delete_by_employee(employee) 

            elif user_input in ['show', '5']:
                empmaster.dept_of_employee() 

    except Exception as e:
        print("e")
    finally:            
        print("Thank you for using our EmployeeMaster System.")


if __name__ == '__main__':
    main()

