"""
Add new employee (ID, name, age, department)

View all employees

Search by employee ID

Delete employee by ID

Show employees grouped by department

save data to file 

load data from file 

Export data to txt, json and csv 

Load data from JSON from startup

# Bonus: add log whenever employee added.
"""
import os 
import pandas as pd 
import logging 
import json 

class EmployeeManager:
    def __init__(self):
        self.emp_detail = dict()
        self.filepath = r"D:\harish\Solo_LvL_SDE\Phrase1\day4"

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

    def save_to_json(self):
        filename = "employees.json"
        try:
            if self.emp_detail:
                with open(os.path.join(self.filepath, filename), 'w') as file:
                    # Serializes a Python object to a JSON Formatted stream and writing it to a file-like object.
                    json.dump(self.emp_detail, file)
            else:
                raise Exception 
            print("File saved as json")
        except Exception as e:
            print(f"Failed to save the file as json: {e}")
        return

    def save_to_txt(self):
        filename = "employees.txt"
        try:
            if self.emp_detail:
                with open(os.path.join(self.filepath, filename), 'w') as file:
                
                    for emp in self.emp_detail:
                        file.write(f"EmployeeID: {emp}; name: {self.emp_detail[emp]['name']}; age: {self.emp_detail[emp]['name']}; dept: {self.emp_detail[emp]['dept']}")
                        file.write('\n')
                    print("File saved as txt")
            else:
                raise Exception
        except Exception as e:
            print(f"Failed to save the file as txt: {e}")
        return
        

    def save_to_csv(self):
        filename = "employees.csv"
        try:
            if self.emp_detail:
                temp_ls_data = []
                for emp in self.emp_detail:
                    temp_data = {}
                    temp_data['EmployeeID'] = emp
                    temp_data['Name'] = self.emp_detail[emp]['name']
                    temp_data['Age'] = self.emp_detail[emp]['age']
                    temp_data['Department'] = self.emp_detail[emp]['dept']
                    temp_ls_data.append(temp_data)
                df = pd.DataFrame(temp_ls_data)
                if df.empty:
                    print("No data to make csv")
                    return 
                else:   
                    # writing into csv format
                    df.to_csv(os.path.join(self.filepath, filename), index=False)
                    print("File saved as csv")
            else:
                raise Exception
        except Exception as e:
            print(f"Failed to save the file as csv: {e}")
        return

    def load_from_json(self):
        filename = "employees.json"
        filepath = os.path.join(self.filepath, filename)
        if os.path.exists(filepath) and os.path.isfile(filepath):
            # Deserialize a JSON Formatted stream to a File-like object (File) to python object.
            try:
                with open(filepath, 'r') as file:
                    self.emp_detail = json.load(file)
                print(f"file loaded into the system.")
                return
            except Exception as e:
                print("Unable to load the file.")
        else:
            print(f"File doesn't exists. Please choose option 1. Add")
        self.emp_detail = {}
        return



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
        6. Save data to file
        7. Load data from file
        OR              
        press Enter to Quit: """)
            
            user_input = user_input.lower().strip()
            if user_input == '' or user_input not in ['add','view','search','delete','show','save','load','1','2','3','4','5','6','7']:
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
            
            elif user_input in ['save','6']:
                empmaster.save_to_json()
                empmaster.save_to_txt()
                empmaster.save_to_csv()

            elif user_input in ['load','7']:
                empmaster.load_from_json()

    except Exception as e:
        print("e")
    finally:            
        print("Thank you for using our EmployeeMaster System.")


if __name__ == '__main__':
    main()

