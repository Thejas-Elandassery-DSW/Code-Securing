from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI() 

class Employee(BaseModel):
    name : str
    age : int
    salary : int
    department : str
    experience : Optional[int] = None


Employees = {
    1 : Employee(name = "John", age = 25, salary = 50000, department = "IT", experience = 3), 
}

app.get("/")
def index():
    return {"message": "Hello World"}

app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return Employees[employee_id]

app.post("/employees/")
def create_employee(employee: Employee, employee_id: int,employee_name: str,employee_age: int,employee_salary: int,employee_department: str,employee_experience: int):
    employee.age = employee_age
    employee.name = employee_name
    employee.salary = employee_salary
    employee.department = employee_department
    employee.experience = employee_experience
    Employees[employee_id] = employee
    return Employees[employee_id]

