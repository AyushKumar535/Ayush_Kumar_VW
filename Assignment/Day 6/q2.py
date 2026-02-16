class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")

    def _financial_report(self):
        print("Accessing confidential financial report...")


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")

    def _policy_update(self):
        print("Updating internal company policies...")



class CompanyAcquisition(Company):
    def __init__(self, name, location, acquired_company):
        super().__init__(name, location)
        self.acquired_company = acquired_company
        self.merged_employees = []

    def merge_employee(self, employee):
        self.merged_employees.append(employee)

    def show_details(self):
        print(f"Company Name: {self.name} (After Acquisition)")
        print(f"Location: {self.location}")
        print(f"Acquired Company: {self.acquired_company}")
        print(f"Total Merged Employees: {len(self.merged_employees)}")



class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


class Manager(NewEmployee):
    def access_financial_report(self, company):
        print(f"{self.emp_name} accessing financial report:")
        company._financial_report()


class HR(NewEmployee):
    def access_policy_update(self):
        print(f"{self.emp_name} updating policy:")
        self._policy_update()


class Developer(NewEmployee):
    pass

class Intern(NewEmployee):
    pass

class ManagerHR(Manager, HR):
    pass

class DeveloperIntern(Developer, Intern):
    pass


if __name__ == "__main__":

    company = Company("TechCorp", "Bangalore")

    manager = Manager(1, "Ayush", "Manager", "01-01-2025", "ABC Ltd")
    hr = HR(2, "Riya", "HR Executive", "02-02-2025", "XYZ Ltd")
    dev = Developer(3, "Karan", "Developer", "03-03-2025", "CodeWorks")
    intern = Intern(4, "Simran", "Intern", "04-04-2025", "StartupX")

    manager.access_financial_report(company)  
    hr.access_policy_update()                 

    manager_hr = ManagerHR(5, "Anita", "ManagerHR", "05-05-2025", "BigCorp")
    manager_hr.access_financial_report(company)
    manager_hr.access_policy_update()

    acquisition = CompanyAcquisition("TechCorp", "Bangalore", "OldTech")
    acquisition.merge_employee(manager)
    acquisition.merge_employee(dev)

    acquisition.show_details()
