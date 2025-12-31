from app.validators.employee_validator import UpdateEmployeePositionValidator

emp_id = 1
data = {
    "position_name":"amele",
    "unit_id":4,
    "name":"mehmet",
    "surname":"yılmaz",
    "started_at":"2025-12-15",
    "ended_at":"2025-10-15",
    "salary":15.000,
    "description":"test employee",
    "is_active":False
}

emp = UpdateEmployeePositionValidator(emp_id,**data)

print(emp.validate())