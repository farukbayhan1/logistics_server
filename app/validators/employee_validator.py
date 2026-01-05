from .base_validator import BaseValidator
from datetime import date, datetime

class CreateGenderValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        gender_name = self.data.get("gender_name")
        if gender_name is None:
            raise ValueError("gender name required")
        if not isinstance(gender_name,str):
            raise ValueError("gender name must be a string")
        
        gender_name = str(gender_name).strip()

        if not gender_name:
            raise ValueError("gender name can not be empty")
        
        if len(gender_name) > 20:
            raise ValueError("gender name must be smaller than 20 characters")
        
        if not gender_name.replace(" ","").isalpha():
            raise ValueError("gender name only contain alphabetic characters")
        
        description = self.description_validate(self.data.get("description"))

        return {
            "gender_name":gender_name.lower(),
            "description":description
        }                                           

class CreateEmployeeUnitValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data
    
    def validate(self):
        unit_name = self.text_validate_lower('unit_name',self.data.get("unit_name"))
        description = self.description_validate('description',self.data.get("description"))
        
        return {
            "unit_name":unit_name,
            "description":description
        }

class CreateEmployeePositionValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        position_name = self.text_validate_lower('position_name',self.data.get("position_name"))
        description = self.description_validate('description',self.data.get("description"))

        return {
            "position_name":position_name,
            "description":description
        }

class CreateEmployeeValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
        self.gender_id = self.single_id_validate('gender_id',self.data.get("gender_id"))
        self.unit_id = self.single_id_validate('unit_id',self.data.get("unit_id"))
        self.position_id = self.single_id_validate('position_id',self.data.get("position_id"))
        self.goverment_id = self._goverment_id_validate(self.data.get("goverment_id"))
        self.name = self.text_validate('name',self.data.get("name"))
        self.surname = self.text_validate('surname',self.data.get("surname"))
        self.started_at = self.date_validate('started_at',self.data.get("started_at"))
        self.salary = self._salary_validate(self.data.get("salary"))
        self.description = self.description_validate('description',self.data.get("description"))

        return {
            "gender_id":self.gender_id,
            "unit_id":self.unit_id,
            "position_id":self.position_id,
            "goverment_id":self.goverment_id,
            "name":self.name,
            "surname":self.surname,
            "started_at":self.started_at,
            "salary":self.salary,
            "description":self.description
        }

    def _goverment_id_validate(self,goverment_id):
        if goverment_id is None:
            raise ValueError("goverment id required")
        
        goverment_id = str(goverment_id).strip()
        if not goverment_id:
            raise ValueError("goverment id can not be empty")
        if len(goverment_id) < 11:
            raise ValueError("goverment id can not be smaller than 11 characters")
        if not goverment_id.isdigit():
            raise ValueError("goverment id only can contain digits")
        
        return goverment_id

    def _salary_validate(self,salary):
        if salary is None:
            return None
        
        if salary:
            if not isinstance(salary,float):
                raise ValueError("salary must be a float")
            if salary < 0:
                raise ValueError("salary can not be smaller than zero")
            
            return salary
        
class CreateEmployeeActivityValidator(BaseValidator):
    def __init__(self,data:dict):
        self.data = data

    def validate(self):
       return self.type_name_validator(self.data)

class UpdateEmployeeValidator(CreateEmployeeValidator):
    def __init__(self,employee_id:int,**kwargs):
        self.employee_id = employee_id
        self.gender_id = kwargs.get("gender_id")
        self.unit_id = kwargs.get("unit_id")
        self.position_id = kwargs.get("position_id")
        self.goverment_id = kwargs.get("goverment_id")
        self.name = kwargs.get("name")
        self.surname = kwargs.get("surname")
        self.started_at = kwargs.get("started_at")
        self.ended_at = kwargs.get("ended_at")
        self.salary = kwargs.get("salary")
        self.description = kwargs.get("description")
        self.is_active = kwargs.get("is_active")

    def validate(self):
        self.single_id_validate('client_id',self.employee_id)
        self._check_updatable_fields()

        data = {}

        if self.gender_id is not None:
            self.single_id_validate('gender_id',self.gender_id)
            data["gender_id"] = self.gender_id
        if self.unit_id is not None:
            self.single_id_validate('unit_id',self.unit_id)
            data["unit_id"] = self.unit_id
        if self.position_id is not None:
            self.single_id_validate('position_id',self.position_id)
            data["position_id"] = self.position_id
        if self.name is not None:
            self.text_validate('name',self.name)
            data["name"] = self.name
        if self.surname is not None:
            self.text_validate('surname',self.surname)
            data["surname"] = self.surname
        if self.started_at is not None:
            self.date_validate('started_at',self.started_at)
            data["started_at"] = self.started_at
        if self.ended_at is not None:
            self.date_validate('ended_at',self.ended_at)
            data["ended_at"] = self.ended_at
        if self.salary is not None:
            self._salary_validate(self.salary)
            data["salary"] = self.salary
        if self.description is not None:
            self.description_validate('description',self.description)
            data["description"] = self.description
        if self.is_active is not None:
            self.is_active_validate('is_active',self.is_active)
            data["is_active"] = self.is_active

        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.gender_id,
            self.unit_id,
            self.position_id,
            self.name,
            self.surname,
            self.ended_at,
            self.salary,
            self.description,
            self.is_active
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field must be provided for update")

class UpdateEmployeePositionValidator(BaseValidator):
    def __init__(self,position_id:int,**kwargs):
        self.position_id = position_id
        self.position_name = kwargs.get("position_name")
        self.description = kwargs.get("description")
    
    def validate(self):
        self.single_id_validate('position_id',self.position_id)
        self._check_updatable_fields()

        data = {}

        if self.position_name is not None:
            self.text_validate_lower('position_name',self.position_name)
            data["position_name"] = self.position_name
        if self.description is not None:
            self.description_validate('description',self.description)
            data["description"] = self.description

        return data
    
    def _check_updatable_fields(self):
        updatable_fields = [
            self.position_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field must be provided for update")

class UpdateEmployeeUnitValidator(BaseValidator):
    def __init__(self,unit_id:int,**kwargs):
        self.unit_id = unit_id
        self.unit_name = kwargs.get("unit_name")
        self.description = kwargs.get("description")

    def validate(self):
        self.single_id_validate('unit_id',self.unit_id)
        self._check_updatable_fields()

        data = {}

        if self.unit_name is not None:
            self.text_validate_lower('unit_name',self.unit_name)
            data["unit_name"] = self.unit_name
        if self.description is not None:
            self.description_validate('description',self.description)
            data["description"] = self.description

        return data

    def _check_updatable_fields(self):
        updatable_fields = [
            self.unit_name,
            self.description
        ]

        if not any(v is not None for v in updatable_fields):
            raise ValueError("at least one field must be provided for update")