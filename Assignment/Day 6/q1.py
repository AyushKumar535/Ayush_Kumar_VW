class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_details(self):
        print(f"\nCompany Name: {self.name}")
        print(f"Location: {self.location}")
        print("Employees:")

        for emp in self.employees:
            emp.show_details()
            print("-" * 40)


class Employee:
    def __init__(self, emp_id, emp_name, designation, **kwargs):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation
        super().__init__(**kwargs)

    def show_details(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


class CompanyAcquisition(Company):
    def __init__(self, name, location, acquired_company_name):
        super().__init__(name, location)
        self.acquired_company_name = acquired_company_name

    def show_details(self): 
        print("\n===== Company Acquisition Details =====")
        print(f"Parent Company: {self.name}")
        print(f"Acquired Company: {self.acquired_company_name}")
        print(f"Location: {self.location}")
        print("\nMerged Employee List:")
        print("=" * 40)

        for emp in self.employees:
            emp.show_details()
            print("=" * 40)

class NewEmployee(Employee):
    def __init__(self, joining_date, previous_company, **kwargs):
        self.joining_date = joining_date
        self.previous_company = previous_company
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


class Manager(NewEmployee):
    def __init__(self, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)
    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, policies_handled, **kwargs):
        self.policies_handled = policies_handled
        super().__init__(**kwargs)
    
    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")


class Developer(NewEmployee):
    def __init__(self, programming_languages, **kwargs):
        self.programming_languages = programming_languages
        super().__init__(**kwargs)
    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")


class Intern(NewEmployee):
    def __init__(self, duration, **kwargs):
        self.duration = duration
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration}")


class ManagerHR(Manager, HR):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def show_details(self):
        super().show_details()
        print("Role: Manager + HR")


class DeveloperIntern(Developer, Intern):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Role: Developer + Intern")



if __name__ == "__main__":

    company = CompanyAcquisition("TechNova", "Bangalore", "SoftSolutions")

    m1 = Manager(
        emp_id=101,
        emp_name="Ayush",
        designation="Project Manager",
        joining_date="01-01-2024",
        previous_company="SoftSolutions",
        team_size=10
    )

    d1 = Developer(
        emp_id=102,
        emp_name="Rahul",
        designation="Software Developer",
        joining_date="15-02-2024",
        previous_company="SoftSolutions",
        programming_languages=["Python", "Java"]
    )

    hr1 = HR(
        emp_id=103,
        emp_name="Ishaa",
        designation="HR Executive",
        joining_date="10-03-2024",
        previous_company="TechNova",
        policies_handled=5
    )

    intern1 = DeveloperIntern(
        emp_id=104,
        emp_name="Aman",
        designation="Developer Intern",
        joining_date="01-04-2024",
        previous_company="SoftSolutions",
        programming_languages=["Python"],
        duration="6 Months"
    )

    company.add_employee(m1)
    company.add_employee(d1)
    company.add_employee(hr1)
    company.add_employee(intern1)
    company.show_details()

