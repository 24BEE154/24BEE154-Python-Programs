print("Name:Shubh Raval")
print("Roll no.:24BEE154")
import pickle
from datetime import date

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def display(self):
        print(f"Emp Code: {self.empcode}")
        print(f"Name: {self.empname}")
        print(f"Date of Joining: {self.doj}")
        print(f"Salary: {self.salary}")

def serialize_employee(emp, filename):
    with open(filename, 'wb') as file:
        pickle.dump(emp, file)
    print(f"✅ Employee data serialized to '{filename}'")

def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        emp = pickle.load(file)
    print(f"\n✅ Employee data deserialized from '{filename}':")
    emp.display()

if __name__ == "__main__":
    
    emp = Employee(empcode="E101", empname="John Doe", doj=date(2021, 5, 10), salary=55000)
    file_name = "employee.dat"
    serialize_employee(emp, file_name)
    deserialize_employee(file_name)
